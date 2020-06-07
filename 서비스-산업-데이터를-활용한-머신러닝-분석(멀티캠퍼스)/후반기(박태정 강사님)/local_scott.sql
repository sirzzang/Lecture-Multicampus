--combine characters
select 'A' || 'B' from dual;
select ename, job from emp;
select ename || job from emp;
select ename || '' || job from emp;

--escape character
select 'A' from dual;
select "A" from dual;
select q'['A']' from dual;

--day, hour, minute, second
select sysdate, sysdate+1, sysdate-1 from dual; --day: 1
select sysdate, sysdate+5/24, sysdate-5/24 from dual; --hour: 24
select sysdate, sysdate+10/1440, sysdate-5/1440 from dual; --minute: 1440
select sysdate, sysdate+10/86400, sysdate-10/86400 from dual; --second: 86400

--column  
select hiredate from emp;
select sysdate-hiredate from emp;

select sal, comm, sal+comm*12
from emp; -- if comm is (null), third column will be (null)

--Q1
desc emp;
select * from emp where deptno = 10;

--Q2
desc emp;
select job from emp;
select * from emp where job='SALESMAN';

--Q3
desc emp;
select hiredate from emp;
select * from emp where hiredate>='1982/01/01';

--Q4
select * from emp where SAL >= 2500;

--null error
select * from emp where comm = null;
select * from emp where comm is null;
select * from emp where comm is not null; --receiving commission
select * from emp where comm >= 0; --comm>=0 means receiving commission

--Q5
select * from emp where sal between 2000 and 3000;
select * from emp where sal >= 2000 and sal <= 3000; --same result

--Q6
select * from emp where job in ('SALESMAN','CLERK');
select * from emp where job ='SALESMAN' or job ='CLERK';

--Q7
select ename from emp where ename like '%N';

--Q8
select ename from emp where ename like '_O%';

--column sort/order
select * from emp; --already ordered by EMPNO

--order by deptno
select empno, ename, sal, deptno from emp order by deptno desc;

--Q9
select empno, ename, deptno, sal*12 as SALARY from emp order by SALARY desc;
select empno, ename, deptno, sal*12 "Annual Salary" from emp order by 4 desc; --column position ok
select empno, ename, deptno, sal*12 as SALARY from emp order by sal*12 desc; --pyohyeonsik ok
select empno, ename, deptno, sal*12 as "Annual Salary" from emp order by "Annual Salary" desc;

--Q10
select * from emp order by deptno asc, sal desc;
select empno, ename, deptno, sal*12 "Annual Salary" from emp order by 3, 4 desc;
select empno, ename, deptno, sal*12 "Annual Salary" from emp order by deptno, 4 desc;

--Q11
select * from emp where empno = &emp_num;

--PRACTICE
--1
select * from emp;

--2
select empno, ename, sal, job from emp;

--3
select sal+300 "Increased Salary" from emp;

--4
select comm from emp;

--5
select ename "NAME", sal "SALARY" from emp;

--6
select ename "NAME", sal*12 "Annual Salary" from emp;

--7
select ename "성 명", sal "급 여" from emp;

--8
select ename||job from emp;

--9
select INITCAP(ename)||' is a '||job from emp;

--10
select ename||' : 1 Year salary = '||sal*12 from emp;

--11
select job from emp;

--12
select DISTINCT job from emp;

--13
select DISTINCT deptno from emp;

--14?????????????????
select distinct deptno, job
from emp;

--15
--select rowid from emp;
select empno, ename, rowid from emp;

--17
select empno, ename, job, sal from emp where sal >= 3000;

--18
select empno, ename, job, sal, deptno from emp where job = 'MANAGER';

--19
select empno, ename, job, sal, hiredate, deptno from emp where hiredate >= '1982/01/01';

--20
select ename, job, sal, deptno from emp where sal between 1300 and 1700;

--21
select empno, ename, job, sal, hiredate from emp where empno in (7902, 7788, 7566);

--22??????????????????????????
select empno, ename, job, sal, hiredate, deptno 
from emp 
where hiredate between '1982/01/01' and '1982/12/31';

--23
select ename, sal
from emp
where ename like 'M%';

--24
select ename, job
from emp
where ename like '_L%';

--25
select empno, ename, job, sal, hiredate, deptno
from emp
where comm is null;

--26
select empno, ename, job, sal, hiredate, deptno
from emp
where sal >= 1100 and job = 'MANAGER';

--28
select empno, ename, job, deptno
from emp
where job not in ('MANAGER', 'CLERK', 'ANALYST');

--29
select empno, ename, job, sal
from emp
where job = 'PRESIDENT' and sal >= 1500 or job = 'SALESMAN';

--30
select empno, ename, job, sal
from emp
where sal >= 1500 and job in ('PRESIDENT', 'SALESMAN'); 

--31
select empno, ename, job, sal, hiredate, deptno
from emp
order by hiredate;

--32
select empno, ename, job, sal, hiredate, deptno
from emp
order by hiredate desc;

--33
select empno, ename, job, deptno, sal
from emp
order by deptno, sal desc;

--34
select empno, ename, hiredate, deptno, job, sal
from emp
order by deptno, job, sal desc;

--35
select distinct deptno, job
from emp
order by job;

--36
select ename, sal, mgr
from emp
order by mgr desc;