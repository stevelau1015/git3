# 创建一个新项目
# 创建dev分支
# (修订后内容如下)


# dev文件一下少了很多在test上做出的更新，切换分支前，需要保存文件的更改(对dev分支做的修改）
# 从dev分支创建test分支
#  开始修改test分支里的文件（对test分支进行的修改）

# 修订时也可以修改代码，新增内容，完成编辑（合并时的状态）

# 以上为 git merge dev的过程，将test合并到dev

# 然后git checkout test 切换到test分支，git merge test，给test分支也包含所有的修改记录

# 再次修改test后，使其合并到19bfcab7 dev的树上


# 上次提交因为head在master上，直接并入master了，实际开发中不应该这样，故退回