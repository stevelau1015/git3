# 创建一个新项目
# 创建dev分支
# 修订后内容如下


# dev文件一下少了很多在test上做出的更新，切换分支前，需要保存文件的更改
# 从dev分支创建test分支
#  开始修改test分支里的文件（对test分支进行的修改）

# 修订时也可以修改代码，新增内容，完成编辑（合并时的状态）

# 以上为 git merge dev的过程，将test合并到dev

# 然后git checkout test 切换到test分支，git merge test，给test分支也包含所有的修改记录

# 再次修改test后，使其合并到19bfcab7 dev的树上

# 修订时也可以修改代码，新增内容，完成编辑

# 为了合并到19bfcab7dev的树上 dev版本进行了第二次修改

# 此次提交用于撤回

# 该版本为退回后的版本，上版本为需要回退test的版本，将该版本继续提交，后与dev合并

# 此时将dev与test合并

# 该过程模拟别人在dev版本已经完成开发后，再如何同步到自己的test分支里

# test 后续开发

# dev后续开发

# 把变更推送到origin上去