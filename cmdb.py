import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs

##############################################
## read CMDB_raw file
##############################################
dic = []
def read_dic(dic):
  with io.open(sys.argv[1], 'r', encoding='utf-8-sig') as f:
    while True:
      line = f.readline()
      if not line: break
      tmp = line.rstrip().split(',')
      dic.append(tmp)
#      print (tmp)
    print "====================="
    print ("Read DIC: " + str(len(dic)))
    print "====================="
    f.close()


##############################################
## read endpoint list
##############################################
svr = []
def read_svr(svr):
  with io.open(sys.argv[2], 'r', encoding='utf-8-sig') as f:
#  svr = f.read().splitlines()
    while True:
      line = f.readline()
      if not line: break
      tmp = line.strip('\n').strip('\r')
      svr.append(tmp)
    print "====================="
    print ("Read Servers: " + str(len(svr)))
    print "====================="
    f.close()


##############################################
## lookup an endpoint 
##############################################
def lookup(svr):
  for j in range (0, len(dic)):
    ip_list = dic[j][1].split(';')
#    print (ip_list)
#    print ("len:" + str(len(ip_list)))
    for m in range(0, len(ip_list)):
      if ip_list[m] == svr: 
#        print (str(m) + " : " + ip_list[m])
        return j
  return -1




##############################################
## main
##############################################
if len(sys.argv) < 3:
  print ("Usage: python cmdb.py {dicfile} {svrfile}")
  print (str(len(sys.argv)))
else:
  read_dic(dic)
  read_svr(svr)

  f = open("output.csv", "w")
  f.write(codecs.BOM_UTF8)
  
  # header
  f.write("IP,C01_Hostname,C02_OS,C03_Vendor,C04_Model,C05_IDC,C06_Room,C07_Row,C08_Rack,C09_Hole,C10_Purpose,C11_Switch,C12_PortType,C13_PortNo,C14_Svc1,C15_Svc2,C16_SvrGrp\n")
  
  # body
  j = 0
  for i in range (0, len(svr)):
    k = lookup(svr[i])
    if k > 0:  
      data = svr[i] + "," + dic[k][0] + "," + dic[k][2] + "," + dic[k][3] + "," + dic[k][4] + "," + dic[k][5] + "," + dic[k][6] + "," + dic[k][7] + "," + dic[k][8] + "," + dic[k][9] + "," + dic[k][10] + "," + dic[k][11] + "," + dic[k][12] + "," + dic[k][13] + "," + dic[k][14] + "," + dic[k][15] + "," + dic[k][16] + "\n"

      f.write(data)
      j+=1

  f.close()

  print "====================="
  print ("Write Servers: " + str(j))
  print "====================="
