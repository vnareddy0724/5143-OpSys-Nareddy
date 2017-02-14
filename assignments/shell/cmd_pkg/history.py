

"""
    Name: history
    Description:
        It stores the history of all commands executed.
    Params: 
        *cmd:List of input commands is an argument.
    Returns: None
""" 

def history(*cmd):
		f=open("history.txt",'r')
		count=len(f.readlines())
		count=count+1
		f=open("history.txt",'a')
		f.write("\n")
		f.write(str(count))
		for x in cmd:
			f.write("\t"+x)
