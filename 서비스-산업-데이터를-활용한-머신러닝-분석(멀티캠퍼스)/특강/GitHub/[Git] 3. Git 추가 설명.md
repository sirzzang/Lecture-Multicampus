

# Git 추가 설명

## 1. commit



 git은 commit을 통해 **이력을 확정하고, hash값을 부여**한다. 그리고 부여된 hash값들을 통해 동일한 commit인지 확인한다.



 commit에는 여러 가지 경우가 있다.

* 변경사항 없음 : working directory  변화 X, staging area 비어 있음.

```bash
$ git commit
nothing to commit, working tree clean
```



* working directory 변경사항 있음 : working directory 변화 O, staging area 비어 있음.

```bash
# staging area에 파일을 add해야 함.
# track되지 않는 파일은 있는데, commit하고 싶으면 add하라는 의미.
$ git commit
Untracked files:
        1001/

nothing added to commit but untracked files present
```



### commit 메시지 작성하기



 add 후 commit 메시지를 작성하지 않거나, 이력이 합쳐질 때 vim 화면이 나온다.



 간단한 vim 사용법은 다음과 같다.



* 편집모드(`i`) : 문서 편집 가능.
* 명령모드(`esc`)
  * `dd` : 해당 줄 삭제.
  * `:wq` :  저장 및 종료.
    
    * `w` : write(저장)
    * `q` : quit(종료)
  * `:q!`: 강제 종료.
    * `q` : quit
    * `!` : 강제
    
    

### log 활용하기

* 다음의 명령어를 활용해 commit 이력과 log를 확인할 수 있다.

```bash
$ git log
$ git log --oneline
$ git log -1
$ git log -1 --oneline
$ git log --oneline --graph
```



1. `$ git log`: commit한 시간, 누가 commit했는지, full name hash값 모두 나온다.

```bash
$ git log

(실행 결과)
student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git log
commit 71155a2e318827b95b20a58e72021a2717cb561d (HEAD -> master)
Author: sirzzang <sirzzang@naver.com>
Date:   Wed Dec 11 09:37:10 2019 +0900
```

 * `HEAD` : 현재 작업하고 있는 commit 이력 및 브랜치에 대한 포인터

   ```bash
   a26b82b (HEAD -> master) Add lee.txt
   # 나는 현재 master 브랜치에 있고,
   # a26b82b 커밋의 상태에 있다.
   ```



2. `$ git log --oneline` : 한 줄로 보여줌.

```bash
$ git log --oneline 

(실행 결과)
a26b82b (HEAD -> master) Add lee.txt
8ed4f94 (feature/signout) Complete signout
97871d5 (origin/master) 집 - main.html

# 나는 master 브랜치에서 a26b82b 커밋을 했고,
# feature/signout 브랜치는 8ed4f94 이력이고,
# 원격저장소(origin/master)는 97871d5 이력이다.
```



3. `$ git log -1`, `$ git log -1 --oneline` :   가장 최근 commit 이력에 대한 log

4. `$ git log --oneline --graph` : commit 이력을 그래프로 나타냄.

![gitloggraph](images/gitloggraph.jpg)





### 직전 commit 메시지 수정



 아래의 명령어는 **commit 이력을 변경**하기 때문에, 조심해야 한다. 공개된 저장소(원격 저장소)에 이미 push된 이력이 있다면, **절대 해서는 안 된다.**



```bash
$ git commit --amend
```

```bash
(실행 결과)

$ git log --oneline
	f2ebe12 (HEAD -> master) add lee.txt
$ git commit --amend
    [master 6f50e40] add lee.txt
     Date: Wed Dec 11 09:37:10 2019 +0900
     1 file changed, 1 insertion(+)
     create mode 160000 1001
$ git log --oneline
	6f50e40 (HEAD -> master) add lee.txt
```



 **commit시 특정 파일을 빠뜨렸을 때**에 이 명령어를 사용한다. 즉, staging area에 특정 파일(`omit_file.txt`)을 올리지 않아서 커밋이 되지 않았을 때 사용한다.

```bash
$ touch omit_file.txt
	# 이 파일이 안 들어갔다면?
$ git add omit_file.txt
$ git commit --amend
	# 직전 이력 수정되면서, 파일 같이 올라감.
	
(실행 결과)
student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        2.txt
        omit_file.txt

nothing added to commit but untracked files present (use "git add" to track)

student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git add 2.txt

student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git commit --amend
[master bd30488] 1.txt 추가, 2.txt 추가
 Date: Wed Dec 11 10:18:02 2019 +0900
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 1.txt
 create mode 100644 2.txt

student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git status

On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        omit_file.txt

nothing added to commit but untracked files present (use "git add" to track)
student@M16046 MINGW64 ~/Desktop/멀캠/web (master)
$ git log --oneline
bd30488 (HEAD -> master) 1.txt 추가, 2.txt 추가
```





## 2. staging area

commit 이력이 있는`1.txt` 파일을 열어서 수정하고, commit 이력이 없는 `3.txt` 파일을 만들고, 열어서 수정한 후, 변화를 비교하자.



* commit 이력 **있는** 파일을 수정한 경우

```bash
$ git status

(실행 결과)
On branch master # master 브랜치에 있다.
Changes not staged for commit: # staged 되지 않은 변경 사항들을 알려준다.
# staged가 아닌 변경사항들을 staged로 바꾸려면,
(use "git add <file>..." to update what will be committed)
# working directory에 있는 변화를 버리려면,
# (예컨대, 작업하고 있는데 루비가 와서 backspace 키 눌러서 다 지웠어...)
# commit 이후에 변경된 사항을 모두 없애 버림.
(use "git restore <file>..." to discard changes in working directory)
    modified:   1.txt

no changes added to commit (use "git add" and/or "git commit -a")
# staging area가 비어 있다는 의미.
# 현재 상태를 알려줌 : commit에 추가될 변화가 없음.
```



* add하고 상태를 확인하자.

```bash
$ git add 1.txt
$ git status

(실행 결과)
On branch master
# commit될 변화 : commit 명령어를 사용했을 때, 아래의 내용이 이력에 남는다.
Changes to be committed:
    # unstage하기 위한 명령어(git add의 반대 작업)
  (use "git restore --staged <file>..." to unstage)
        modified:   1.txt
```



* commit 이력 **없는** 파일을 수정한 경우

```bash
$ git status

(실행 결과)
On branch master

# tracking되고 있지 않은 파일 : commit(이력)에 한 번도 관리된 적이 없다.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        3.txt
        uncommit.txt
    # commit할 것도 없고(staging area가 비어 있고),
    # tracking 되고 있지 않은 파일도 있다.
nothing added to commit but untracked files present (use "git add" to track)
```



### add 취소

```bash
$ git restore --staged <file>
```

구 버전 git에서는 아래의 명령어를 사용해야 한다.

```bash
$ git reset HEAD <file>
```



### working directory의 변화 삭제



git에서는 모든 commit된 내용은 되돌릴 수 있다. 다만, 아래의 working directory 내용을 삭제하는 것은 *되돌릴 수 **없다**.*

```bash
$ git restore <file>
```

구 버전 git에서는 아래의 명령어를 사용해야 한다.

```bash
$ git checkout -- <file>
```



## 3. Stash



 stash는 변경 사항을 임시로 저장해 놓는 공간이다.



### 예시 상황

1. feature branch에서 a.txt를 변경 후 commit.

2. master branch에서 a.txt를 수정(add / commit X).

3. merge



* 위와 같은 예시 상황에는 다음과 같은 에러 메시지가 뜬다.

```bash
$ git merge test
# 현재 merge 명령어로 인해 아래의 파일이 덮어쓰여질 수 있다.
error: Your local changes to the following files would be overwritten by merge:
	a.txt
# commit을 하거나 -> 이력 확정을 해서 merge시 충돌 나는 상황으로!
# stash 해라 -> Working directory를 잠시 비워놓음.
Please commit your changes or stash them before you merge.
Aborting
Updating 4d56f57..b8f2357
```



### 예시 상황 해결

```bash
$ git stash # stash 공간에 저장

(실행 결과)
Saved working directory and index state WIP on master: 4d56f57 a.txt

$ git stash list # stash 공간 내용 확인(목록)

(실행 결과)
stash@{0}: WIP on master: 4d56f57 a.txt

$ git stash pop # stash 공간에서 적용(apply)하고 목록에서 삭제(drop)하기

(실행 결과)
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (d82f2fc5a0b5f551ca4484c9aa806b8e398ce350)
```

```bash
$ git stash
$ git merge test
$ git stash pop

# 충돌 해결 후 작업 이어나가기
첫 번째 내용
<<<<<<< Updated upstream
test 브랜치 내용
=======
test 브랜치 내용

a.txt를 브랜치에서수정 후 커밋
master 브랜치에서 수정 중
merge -> merge 안 됨
>>>>>>> Stashed changes
```

* 작업 공간 clean해지고, merge하는데 당연히 충돌이 난다.
* `a.txt` 열어 보면 당연히 충돌 나서 `updated`, `current`로 나뉘어 있다.



### reset vs. revert

* commit 이력을 되돌리는 작업을 한다. 

* `reset` : 이력을 삭제한다.
  * `--mixed`  : 기본 옵션. 해당 커밋 이후 변경사항 staging area에 보관.
  * `--hard` : 해당 커밋 이후 변경사항 모두 삭제. **"돌이킬 수 없으므로" 주의**
  * `--soft` : 해당 커밋 이후 변경사항 및 working directory 내용까지 모두 보관.

``` bash
(실행 결과)

(이전 작업 - 깨끗하게)

student@M16046 MINGW64 ~/Desktop/stash (master)
$ git status
On branch master
Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M16046 MINGW64 ~/Desktop/stash (master)
$ git add .

student@M16046 MINGW64 ~/Desktop/stash (master)
$ git commit
Aborting commit due to empty commit message.

student@M16046 MINGW64 ~/Desktop/stash (master)
$ git commit -m 'a.txt'
[master cb376ee] a.txt
 1 file changed, 9 insertions(+), 1 deletion(-)

student@M16046 MINGW64 ~/Desktop/stash (master)
$ git status
On branch master
nothing to commit, working tree clean
```



* `revert` : 되돌렸다는 이력을 남긴다.

``` bash
$ git log --oneline

(실행 결과)
5743e9c Revert "a.txt test"
984f0f7 a.txt
b8f2357 (test) a.txt test
4d56f57 a.txt
```
