import jieba
import operator


def get_word_freq(path):
    f = open(path,'r')
    f2 = open('./text/stop_word.txt','r')
    lines2 = f2.readlines()

    stop_word_dict = set()
    for l in lines2:
        stop_word_dict.add(l.strip())
    d = {}
    lines = f.readlines()
    sum_words = 0
    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)
        for w in seg_list:
            if w in stop_word_dict:
                continue
            sum_words+=1
            if w in d:
                i = d[w]
                d[w] = i+1
            else:
                d[w] = 1
    for w in d:
        d[w] = float(d[w])/float(sum_words)
            
    return d



def get_word_posibility2():
    f = open('model4.txt','r')
    lines = f.readlines()
    d = {}
    for line in lines:
        #print(line)
        l = line.strip().split(':')
        #print(l)
        if len(l) != 2: continue
        w = l[0]
        p = l[1]
        d[w] = float(p)
    return d


def get_word_posiblity():
    ad_path = './text/ad'
    notad_path = './text/not_ad'
    ad_dict = get_word_freq(ad_path)
    notad_dict = get_word_freq(notad_path)
    d = {}
    for w in ad_dict:
        ph = 0.001
        if w in notad_dict:
            ph = notad_dict[w]
        p = ad_dict[w]*0.5/(ad_dict[w]*0.5 + ph*0.5)    
        d[w] = p
        #print(p)
    return d

def get_top5(stop_word_dict, d, sentence):
    p_list = []
    print('------start------------')
    #print(sentence)
    seg_list = jieba.cut(sentence, cut_all=False)
    duplicate = set()

    sum = 0
    for w in seg_list:
        if w in duplicate: continue
        if w in stop_word_dict: continue
        sum += 1
        if w in d:
            print(w + str(d[w]))
            p_list.append(d[w])
        else:
            p_list.append(0.1)
        duplicate.add(w)
    
    
    print("length "+str(int(sum/2)))    
    res = sorted(p_list,reverse = True)
    while len(res)<sum/2:
        res.append(0.5)
    res2 = res[0:int(sum/2)]
    #print("==============")
    print(res2)
    p1 = 1
    p2 = 1
    for p in res2:
        p1 *= p
        p2 *= (1-p)
    p3 = p1/(p1+p2)

    return p3
    


if __name__=='__main__':

    f2 = open('./text/stop_word.txt','r')
    lines2 = f2.readlines()

    stop_word_dict = set()
    for l in lines2:
        stop_word_dict.add(l.strip())
    d = get_word_posibility2()
    '''
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    for w in reversed(sorted_d):
        print(w[0]+":"+str(w[1]))
    '''
    sentence = "打开12306官方网站，在左侧菜单点击“售票”并登陆12306帐号"
    #sentence = "西藏紧盯群众身边的不正之风和腐败问题 "
    p = get_top5(stop_word_dict, d, sentence)
    print(p)
        
    f_ad = open('./text/ad','r')

    lines = f_ad.readlines()
    c = 0
    c1 = 0
    for line in lines:
        p = get_top5(stop_word_dict, d, line)
         
        if p > 0.7:
            print(line)
            print(str(p))
            print('-----------------')
            c += 1
        if p <= 0.7: 
            c1 += 1
            print(line)
            print(str(p))
            print('-----------------')
        #print('=================')
        #print(line.strip())
        #print(str(p))
        #print('-----------------')    
    print(c)
    print(c1)
    
