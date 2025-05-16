import torch
print(torch.cuda.is_available())       # should return True
print(torch.cuda.device_count())       # should show 4
print(torch.cuda.get_device_name(0))   # should be Tesla V100