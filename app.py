import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from make_upload import drive

class MonitorFolder(FileSystemEventHandler):
    FILE_SIZE=1000
    
    def on_created(self, event):
        print(event.src_path, event.event_type)
        # self.checkFolderSize(event.src_path)
   
    def on_modified(self, event):
        print("Hello")
        # print(event.src_path, event.event_type)
        # print(event.src_path.strip())
        # self.checkFolderSize(event.src_path)
    
                  
    def checkFolderSize(self,src_path):
        if os.path.isdir(src_path):
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("Time to backup the dir")
                f = drive.CreateFile({'title': src_path})
                f.SetContentFile(src_path)
                f.Upload()
                f = None
        else:
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("very big file")

if __name__ == "__main__":
    src_path = sys.argv[1]
    
    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")
    observer.start()
    try:
        while(True):
           time.sleep(1)
           
    except KeyboardInterrupt:
            observer.stop()
            observer.join()