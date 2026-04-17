mode = "PROD"

if mode == "local":
    LOGPATH = r"/Users/himanshusakwaya/Desktop/work projects/Sroniyan/internal/projects/srn-analyst-app/drive/logs"
    KEYFILE_PATH = r"/Users/himanshusakwaya/Desktop/srn/2022-10/04/jwt_key.txt"
elif mode == "DEV":
    LOGPATH = r"/home/ubuntu/app/python-ms/analyst-app/dev-ms/drive/logs"
    KEYFILE_PATH = r"/home/ubuntu/app/python-ms/analyst-app/dev-ms/drive/data/jwt_key.txt"
elif mode == "PROD":
    LOGPATH = r"/home/ubuntu/app/python-ms/analyst-app/drive/logs"
    KEYFILE_PATH = r"/home/ubuntu/app/python-ms/analyst-app/drive/data/jwt_key.txt"
else:
    LOGPATH = r"/home/maneesh/My_Work/StrateSphere/SS-Microservices/drive/in"
    KEYFILE_PATH = r""
