import os
def all_mp3_files(h):
    main_list=[]
    for a,b,c in os.walk(h):
        if len(c)>0:
            for i in c:
                if i[-1]=='3':
                    main_list.append(a+i)
    return main_list
