import pandas as pd

source = ["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
# 課題１
    if word in source :
        print('{}が見つかりました。'.format(word))
    else:
        print('{}が見つかりません。'.format(word))
# 課題２
        source.append(word)
        print('{}を追加しました。'.format(word))
        print('追加後の登場人物は{}です。'.format(source))

def search_write_name():
# 課題３
    df_source = pd.DataFrame(source)
    df_source.to_csv('source.csv')
    df_name = pd.read_csv('source.csv')
    names = df_name['0'].tolist()
    print('souce.csvから読み込んだ登場人物は{}です。'.format(names))

# 課題４
    name = input("鬼滅の登場人物の名前を入力してください >>> ")

    if name in names:
        df_names = pd.DataFrame(names)
        df_names.to_csv('names.csv')
        print('{}が見つかりました。names.csvを確認してください。'.format(name))
    else:
        print('{}が見つかりません。'.format(name))
        names.append(name)
        df_names = pd.DataFrame(names)
        df_names.to_csv('names.csv')
        print('{}を追加しました。names.csvを確認してください。'.format(name))

if __name__ == "__main__":
    search()
    search_write_name()