# -*- coding:utf-8 -*-
import requests
import json
import platform
import getpass
import linecache
import logger
log = logger.get_logger('Githandler')
# print(platform.platform()) # Windows-10-10.0.17134-SP0 # Linux-4.18.20-1.el6.elrepo.x86_64-x86_64-with-centos-6.9-Final

class Git(object):
    def __init__(self, accessToken):
        self.accessToken = accessToken
        self.rootUrl = 'https://api.github.com'
        self.headers = {"Authorization": "token %s" % self.accessToken}


    def check_json_format(self, raw_msg):
        """
        :return:
        """
        if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
            try:
                json.loads(raw_msg, encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            return False

    def baseGet(self, url, me='get', data=None):
        try:
            response = ''
            if me == 'get':
                response = requests.get(url)
            if me == 'post':
                response = requests.post(url, data=data, headers=self.headers)
            if me == 'delete':
                response = requests.delete(url, headers=self.headers)
            try:
                data = response.json()
            except:
                data = response.content
            return data
        except Exception as e:
            log.error('error by', e)
            return False


    def get_roteNum(self):
        log.debug(u'get api use nums in one hour')
        roteUrl = self.rootUrl + '/rate_limit?access_token=%s' % self.accessToken
        return self.baseGet(roteUrl)

    def get_repro(self, uesrname):
        reps = self.rootUrl + '/users/%s/repos?access_token=%s' % (uesrname, self.accessToken)
        return self.baseGet(reps)

    def get_flowwer(self, username):
        flowers = self.rootUrl + '/users/%s/followers?access_token=%s' % (username, self.accessToken)
        print(flowers)
        return self.baseGet(flowers)
    def get_public_key(self):
        # return all public key
        allkeys = self.rootUrl + '/user/keys?access_token=%s' % (self.accessToken)
        print(allkeys)
        return self.baseGet(allkeys)
    def get_user_public_key(self, username):
        userkey = self.rootUrl + '/users/%s/keys?access_token=%s' % (username, self.accessToken)
        # print(userkey)
        return self.baseGet(userkey)

    def del_user_public_key(self, key_id):
        # del_user_public_key
        userkey = self.rootUrl + '/user/keys/%d?access_token=%s' % (key_id, self.accessToken)
        print(userkey)
        return self.baseGet(userkey, me='delete')

    def read_public_key(self, path=None, public_id_file='id_rsa.pub'):
        # print('ok')
        if platform.system().lower() == 'windows':
            if not path:
                content = ''
                paths = 'C:/Users/%s/.ssh/%s' % (getpass.getuser(), public_id_file)
                cache_data = linecache.getlines(paths)
                for line in range(len(cache_data)):
                    content += cache_data[line]
                return content
        else:
            # Linux|mac
            pass

    def add_user_public_key(self, title, path=None, public_id_file='id_rsa.pub'):
        public_id = self.read_public_key(path, public_id_file)
        # print(public_id)
        add_key = self.rootUrl + '/user/keys?access_token=%s' % self.accessToken
        # print(add_key)
        postData = {"title": title, "key": public_id}
        log.info(postData)
        return self.baseGet(add_key, me='post', data=json.dumps(postData))

    def get_all_repos(self):
        repos = self.rootUrl + '/user/repos?access_token=%s' % self.accessToken
        return self.baseGet(repos)

    def delete_one_repo(self, owner, repo):
        delete_url = self.rootUrl + '/repos/%s/%s' % (owner, repo)
        return self.baseGet(delete_url, me='delete')

    def create_one_repo(self, **kwargs):
        # detail
        # print(kwargs)
        create_repo_url = self.rootUrl + '/user/repos'
        if not kwargs['name'] or not kwargs['description']:
            log.error(u'you should pass the name or description ')
            return
        else:
            return self.baseGet(create_repo_url, me='post', data=json.dumps(kwargs))




