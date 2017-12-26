import thulac

thu1 = thulac.thulac(seg_only=True)

text = thu1.cut("活动二 ：11月29日 - 12月1日，吃喝窝窝(微信号:chihewowo)/吃喝阿呆(微信号:chihedai)朋友圈将有活动，选出2位幸运饿魔，每人可获得由恋尚千层提供的榴芒千层蛋糕一份。", text=True)

print(text.split(' '))
