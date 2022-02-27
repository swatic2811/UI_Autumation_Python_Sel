import logging
import sys
from logging import Logger

exec_logging_format = "%(asctime)s - %(module)s - %(lineno)d - %(levelname)s - %(message)s"


class LOGGER(Logger):
   log_exe = None
   log_root = None

   def __init__(self,log_file =None,logger_name='exec',*args,**kwargs):
      Logger.__init__(self,logger_name,*args,**kwargs)
      log_format = exec_logging_format
      self.log_file = log_file
      self.formatter = logging.Formatter(log_format)
      self.addHandler(self.get_console_handler())
      if log_file:
         self.addHandler(self.get_file_handler())
      self.propagate = False

   def get_console_handler(self):
      console_handler = logging.StreamHandler(sys.stdout)
      console_handler.setFormatter((self.formatter))
      return console_handler

   def get_file_handler(self):
      file_handler = logging.FileHandler(filename=self.log_file)
      file_handler.setFormatter(self.formatter)
      return file_handler

   @staticmethod
   def set_logger(log_file='',logger_name='exec'):
      logging.setLoggerClass(LOGGER)
      LOGGER.log_exe = LOGGER(log_file=log_file,logger_name=logger_name)
      LOGGER.log_exe.info("test")

   @staticmethod
   def get_logger(logger_name='exec'):

      if logger_name =='exec':
         return LOGGER.log_exe
      else:
         return LOGGER.log_root