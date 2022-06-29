import multiprocessing as mp
import subprocess
from tabulate import tabulate

global data

def run_shell_cmd(sh_cmd):
    print("running cmd {}".format(sh_cmd))
    cmd_list = sh_cmd.split(" ")
    try:
        result = subprocess.check_output(cmd_list).decode()
    except Exception as e:
        result = "command error: {}".format(str(e))
    return (sh_cmd, result)

def get_results(output):
    sh_cmd = output[0]
    result = output[1]
    global data
    if "error" in result:
        return
    else:
        data.append([sh_cmd, result])

if __name__ == "__main__":
    # Create shared memory for parallelized processes
    dm = mp.Manager()
    data = dm.list()

    # create pool of workers for parallelizing run_shell_cmd()
    cpu_count = mp.cpu_count() - 1
    if cpu_count > 0:
        pool = mp.Pool(cpu_count)
    else:
        pool = mp.Pool(1)
    
    sh_cmds = ["whoami","pwd","ls -la"]
    for sh_cmd in sh_cmds:
        # start parallel asynchronous execution of shell cmds
        pool.apply_async(run_shell_cmd, args=(sh_cmd,), callback=get_results)
    
    # wait for workload to finish
    pool.close()
    pool.join()

    # sort by arg
    data = sorted(data, key=lambda x: x[0])

    # tabulate data and store in an HTML table
    print(tabulate(data, headers=["shell cmd", "result"]))
    html_table = tabulate(data, headers=["shell cmd", "result"], tablefmt="html")

    # write html
    f = open("./node_data.html", "w")
    f.write(html_table)
    f.close()

