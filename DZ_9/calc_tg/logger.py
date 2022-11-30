from datetime import datetime as dt



def logger(text,mes, id, fname):
    time = dt.now().strftime("%H:%M:%S")
    log_string = f"{time}; {text}; {mes}; {id}; {fname};\n"
    with open("log.csv", "a") as file:
        file.write(log_string)



