def addnote():
    kok=input('letter put')
    file=open('youu.txt','a')
    file.write(kok+'\n')
    print('saved')
    file.close()
    
def shownote():
    file=open('youu.txt','r')  
    print(file.read())
    file.close()
    
def deletenote():
    confirm=input('are you sure,yes/no')
    if confirm=='yes':
     file=open('youu.txt','w')  
     file.close()
     print('all note deleted')
    
    else:
        print('delete cancelled')
    
while True:
        print('1.addnote')
        print('2.viewnote')
        print('3.deletenote')
        print('4.exit')
        
        dbb=input('choose:')
        if dbb=='1':
            addnote()
        
        elif dbb=='2':
            shownote()
        
        elif dbb=='3':
            deletenote()  
              
        elif dbb=='4':
            print('goodbye')
            break
            
        else:
            print('wrong')           
        