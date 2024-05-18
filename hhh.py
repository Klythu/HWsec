
import nmap
#были проблемы с путем для программы и работает медленно ... ну ничего можно было бы еще список портоворганизовать
start = 1
notclosed=[]
end = 65536
# все кто есть
net = '127.0.0.1'
scanner = nmap.PortScanner() 
for i in range(start,end+1): 
    res = scanner.scan(net,str(i)) 
    if res['scan'][net]['tcp'][i]['state']!="is closed.":
        notclosed.append(res)
#добавил потом можно с ним чтото сделать 
    res = res['scan'][net]['tcp'][i]['state'] 
    print(f'port {i} is {res}.') 