class test:
	para1="class_variable1"
	__private = "private_variable"

	def __init__(self) -> None:
		self.para1 = "instance_variable1"
		self.para2 = "instance_variable2"  # unavailable until instantiated.

	def print(self):
		print(self.para1)


	@classmethod  # Convert a function to be a class method.
	def class_print(cls):
		print(cls.para1, test.para1) # only print class variable.


	@staticmethod  # this func only use class domain name "test".
	def static_print(x):
		print(x)


test().print()
test.class_print()
test.para1=123213
test.class_print()
test.static_print('static method')

func = lambda x, y=0: x+y
print(func(1,2))

try:
	print("try/except: try block")
	raise ConnectionResetError("ConnectionResetError")
except (BaseException, Exception) as e:
	print(e)
	raise
else:
	print("try/except: else block")
finally:
	print("try/except: finally block")