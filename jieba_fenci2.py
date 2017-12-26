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
    f = open('model.txt','r')
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
        #print(w+':'+str(p))
    return d

def get_top5(stop_word_dict, d, sentence):
    p_list = []
    #print('------start------------')
    #print(sentence)
    seg_list = jieba.cut(sentence, cut_all=False)
    duplicate = set()
    for w in seg_list:
        if w in duplicate: continue
        if w in stop_word_dict: continue
        if w in d:
            #print(w + str(d[w]))
            p_list.append(d[w])
        else:
            p_list.append(0.5)
        duplicate.add(w)
    
    

    res = sorted(p_list,reverse = True)
    while len(res)<5:
        res.append(0.5)
    res2 = res[0:5]
    #print("==============")
    #print(res2)
    p1 = 1
    p2 = 1
    for p in res2:
        p1 *= p
        p2 *= (1-p)
    p3 = p1/(p1+p2)

    return p3
    


if __name__=='__main__':
    d = get_word_posiblity() 
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    for w in reversed(sorted_d):
        print(w[0]+":"+str(w[1])) 
