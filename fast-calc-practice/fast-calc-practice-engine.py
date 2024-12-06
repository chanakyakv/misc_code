
import random
import time
import winsound

# from rich.console import Console
# from rich.text import Text
# console = Console()
# text = Text("hello world")
# text.stylize("bold red size=20")
# console.print(text)

ops={
    1:["singled_plus_singled",[2,9,1],[2,9,1],"+"],
    2:["doubled_plus_singled",[10,99,1],[2,9,1],"+"],
    # 3:["trippled_plus_singled",[100,999,1],[2,9,1],"+"],
    # 4:["trippled_plus_doubled",[100,999,1],[10,99,1],"+"],
    # 3:["singled_into_singled",[2,9,1],[2,9,1],"*"],
    # 4:["doubled_into_5multiples",[2,20,1],[5,10,5],"*"],
    # 5:["double_of_5multiples",[5,1000,5],[2,2,1],"*"],
    # 6:["half_of_10multiples",[10,1000,10],[2,2,1],"/"],

}

def gen_rand(range_list):
    if range_list[0]==range_list[1]:
        return range_list[0]
    return random.randrange(range_list[0],range_list[1],range_list[2])

def average_last_n(lst, n):
  """Calculates the average of the last n elements in a list.
  Args:
    lst: The list of numbers.
    n: The number of elements to average.
  Returns:
    The average of the last n elements.
  """
  # print(lst)
  if len(lst)==0:
    return 0.00
  if n=="all" and len(lst)>=1:
      return round(sum(lst) / len(lst), 2)
  if n > len(lst):
    return 0.00
  return round(sum(lst[-n:]) / n, 2)

def eliminate(n1,op_str,n2,times_dict):
    tuple1=tuple([n1,op_str,n2])
    # if n1+n2<=5:
    #     return True
    if tuple1 in times_dict:
        if len(times_dict[tuple1])>=3:
            max_last_three_times=max(times_dict[tuple1][-3:])
            if max_last_three_times<2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

class c:
    M = '\033[95m'
    B = '\033[94m'
    C = '\033[96m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    BLD = '\033[1m'
    UND = '\033[4m'
alarm_seconds=1
alarm_duration=1000

count=0
times=[]
times_dict=dict()

while(1):
    opn=gen_rand([1,len(ops.keys())+1,1])
    n1=gen_rand(ops[opn][1])
    n2=gen_rand(ops[opn][2])
    op_str=ops[opn][3]
    answer_correct=False
    answer_time=0
    if eliminate(n1,op_str,n2,times_dict):
        continue
    count=count+1
    while(not answer_correct):
        print("---------------------------------------------")
        print("")
        print("+---+---+---+---+---+---+---+---+---+---+---+")
        print(c.B+"Seconds Taken per operation (last 1,2,3,5,10,all("+str(count)+") additions moving averages): ",average_last_n(times,1),average_last_n(times,2),average_last_n(times,3),average_last_n(times,5),average_last_n(times,10),average_last_n(times,"all"),""+c.E)
        print("+---+---+---+---+---+---+---+---+---+---+---+")
        print("")
        print("+---+---+---+---+---+---+---+---+---+---+---+")
        print("")
        print(c.Y+"Question: "+c.BLD+str(n1)+" "+op_str+" "+str(n2)+c.E)
        print("Answer: ?? ")
        start = time.time()*1000
        answer=input()
        # time.sleep(1)
        end = time.time()*1000
        time_elapsed_in_ms=end-start
        answer_time=answer_time+time_elapsed_in_ms
        time_elapsed_in_seconds=round(answer_time/1000, 2)
        print(f"{time_elapsed_in_seconds =}")
        try:
            int_answer=int(answer)
        except:
            print(c.R+"Wrong!"+c.E)
            #print("Answer: ?? ")
            winsound.Beep(1000, 700)
            continue
        expected_answer=eval(str(n1)+op_str+str(n2))
        # print(expected_answer)
        if int(answer)==expected_answer:
            answer_correct=True
            winsound.Beep(3000, 100)
            times.append(time_elapsed_in_seconds)
            tuple1=tuple([n1,op_str,n2])
            if not (tuple1 in times_dict):
                times_dict[tuple1]=[time_elapsed_in_seconds]
            else:
                times_dict[tuple1].append(time_elapsed_in_seconds)
            print(times_dict)
            print(c.G+"Correct!"+c.E)
        else:
            print(c.R+"Wrong!"+c.E)
            #print("Answer: ?? ")
            winsound.Beep(1000, 700)

