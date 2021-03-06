"""
    分支管理:
        git branch (查看分支情况)
        git branch 分支名  (创建分支,在那个分支上创建就是基于那个分支创建的)
        git checkout 分支名 (切换到某一分支)
        git checkout -b 分支名 (创建并切换到分支)
        git merge 分支名  (将该分支合并到当前分支)
        git branch -d 分支名  (删除分支，只有分支被合并后才能删除)
        git branch -D 分支名  (删除分支，分支没有被合并也能被删除)

        冲突问题:
            一个分支向另一个分支合并的过程中，发现原分支已经发生了变化，就会产生冲突。
            因为git是逐行合并的，如果两条分支在同一行的内容不同，就会产生冲突，这需要你自行解决,
            打开冲突文件手动删除，并保存

    远程仓库:
        拉取仓库:
            git clone 仓库地址
        上传仓库:
            git push -u 仓库名 分支名 (第一次上传一个分支时要加-u,加了-u会将本地分支与远程库分支建立一个关联,
            以后上传，直接git push，不加仓库名和分支名，默认就是这个远程仓库的这个分支)

            git push (有了上一步之后，使用此命令会自动将对应分支(有几个关联，
            修改几个分支就都会被上传合并)的修改内容进行上传合并)

            gir branch -a 查看关联与分支
            git push 库名 :分支名  (删除远程分支)

            git push 库名 tag_name  上传标签

            如果本地版本落后于远程库版本，并且要将落后版本上传至远程库，可以用下面的命令强行推送
            git push --force 库名



        创建远程仓库，并上传项目:
            git remote add 远程仓库名称 远程库地址  (连接一个远程库，并取一个别名)
            git remote (查看关联的远程库)
            git remote rm 远程仓库名称  (断开与远程库的连接)

        github的使用:
            搜索框:

        拉取操作:
            git pull 仓库名 分支名 (拉取到本地并合并)(如果已经建立关联，直接git pull就行了)
            git fetch 库名 分支名:临时分支名  (拉取远程库更新，并在本地创建一个分支，不合并)

        删除远程仓库:
            我的仓库，settings ，最下面，


"""