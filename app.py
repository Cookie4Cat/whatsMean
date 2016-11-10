from urllib import request
import json,sys

def get_youdao_translate(api,word):
    url = api + word
    req = request.Request(url)
    with request.urlopen(req) as f:
        resp = str(f.read().decode('utf-8'))
        j = json.loads(resp)
        for mean in j['basic']['explains']:
            print(mean,end='\n')
if __name__ == '__main__':
    with open(sys.path[0] + '/config.json') as f:
        config = json.load(f)
    youdaoApi = config['youdaoApi']
    words = ''
    for word in sys.argv[1:]:
        words += word
    get_youdao_translate(youdaoApi,words)