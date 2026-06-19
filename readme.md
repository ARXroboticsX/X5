# X5 python SDK

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTFhMzIzNmZlY2I4ZWRhNTYyZDNiMGRkYmE5NTBiNTBfMzJjYmJjYjIyNDJmNTI1YmJmNmZjMmIwNzgyNjUxMzJfSUQ6NzYzMzY3MTUwMzU1NDE4NjE3MF8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

使用机械臂时，务必确保安装稳定，以基座为轴心一米半径内确保空旷，当心碰撞易碎物品及造成人员损伤。出现紧急情况请先关闭电源。

# 型号区分

|型号||示意图|区别|
|---|---|---|---|
|X5（2023）|标准单臂<br>|![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDVkYjM5OGJhODJhYWEwZTNiMDJhYzA2YWRhYTQ1MmNfOTNiODNmYmU4N2QxZTM0YmY4M2VjMTgyM2Y0M2NhZGNfSUQ6NzYzMzY3MTY3NjM3ODk0MjY4Nl8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)|单轨二指夹爪|
|X5（2025）<br>|AC one上机械臂<br>|![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yjk2NmE5OTc1ZjFlYjk4MjE4ZDhhOWU4M2VkZTYzN2VfNGIyY2U2NGQ0Y2UzMzMwOTUxOGNjYWE0MjhmYTRlMmNfSUQ6NzYzMzY3MTY3NTk2NzgxODk0Ml8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)|双轨二指夹爪|

# 仓库地址

https://github\.com/ARXroboticsX/X5\.git

# 00硬件设备连接

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjI2NWUzNTZhYzJlMjcxOGYwYjA3NjE2OGZjOWY0MzdfZjU0ZjIyYTAyMTAyZmNjZjlhMTdiMWJjM2Q3ZTIzNTRfSUQ6NzYzMzc2NjYwMTQwMTYxNzYxNV8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTEyNzlmMTA0N2E3NzIwMjNjODA5YjE4ZTQ2MTgxYWRfMWYzMDA0YTBjNWNhZjVkYzk2MjYwOGQ1NzAzZDY4MGVfSUQ6NzYzMzc2NjYwNDA5Mzg1Mjg3MF8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

# 00环境配置

ARX\_X5/tools/

```Plain Text
./01_global_nopasswd_sudo.sh.x
./02install.x
./03_install_common_packages.sh.x 
```

# A配置CAN设备

设备如未更改，只需配置一次即可

多个设备设置时，需要逐个拔插。每次操作只有一台CAN设备在线。

ARX\_X5/ARX\_CAN/

```Plain Text
./search
```

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yjc1ZDE4ZjYzNmVjMTdmMDFmNmU1MDU1ZmVlZTI3ZDVfYmZjNWY2NTFjNTgzMTUxYmExZGIwOTIyMjJjMDQ0ZjlfSUQ6NzYzMzMwNjk1MzI5MjQ4MzUzNl8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

Copy number to arx\_can\.rulels,and save

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWQzMGQzMDk0M2EyMGRhZTdjODhmZjdhNWNjNmNlYTFfMTMzOTc3MDFlZTcyYjU1NTE0NjRlNDA0Y2EzN2E2ZDZfSUQ6NzYzMzMwNjk1Mjk4NjUxMjMxNl8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

```Plain Text
./set
```

Start can

Cd arx\_can,start the number which you want\.

```Plain Text
./arx_can1
```

# B编译

ARX\_X5/py/arx\_x5\_python/

```Plain Text
./build.sh
```

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2Q3Y2Q2MDQwYmU1YzM4MGVhZTc5MzY5ZGNkMjZlY2NfYTQwOWIwZmRiNjg5YWI4MjY3OTllMGQwZTM2NGExZGFfSUQ6NzYzMzMwNjk1MzgwODUxNDAxMl8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

# C运行

ARX\_X5/py/arx\_x5\_python/

```Plain Text
source ./setup.sh
python3 test_single_arm.py
```

# SDK

## 0\>夹爪控制

set\_gripper\_pos\(\)  

|类型|夹爪范围|
|---|---|
|X5\-2023|0,5|
|X5\-2025|\-3\.14，0|

## 1\>姿态控制

set\_ee\_pose\_xyzrpy\(xyzrpy\)

## 2\>关节位置控制（底层重力补偿）

set\_joint\_positions\(positions\)

## 3\>状态反馈

关节反馈（位置，速度，扭矩）\+姿态反馈

### 3\.1 关节位置反馈

get\_joint\_positions\(\)

### 3\.2 关节速度反馈

get\_joint\_velocities\(\)

### 3\.3 关节扭矩反馈

get\_joint\_currents\(\)

### 3\.4 末端位姿反馈

get\_ee\_pose\_xyzrpy\(\) 欧拉角形式

## 4\>重力补偿

gravity\_compensation\(\)

默认值仅含夹爪。加装摄像头等设备后，如遇到末端坠落，或者抬升。请参照\<6\>更改末端质量

若抬升，请调低数值

若下降，请调高数值

## 5\>根据关节位置，解算出姿态

forward\_kinematics\(\)

## 6\>更改末端质量

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzljNzYwOTVlY2RjZDIzYWY4NmUwM2ZjZWE4M2U2OGZfMjhkZjU3NjA1ZjBiNWE4Y2U4MjIyOTA5NjQ2ZjQ4N2JfSUQ6NzYzMzc2MjMzMjYwNjk5MTMwOF8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

Change link6 mass

Remember to save

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjNmOGEwZjVjYzMxNGQ2ODQwYTZjOGY4MGVkYjcwZmRfMjgwYTg2Yzk2MDk4ZTM2YWIzZTI3ODFjYjY1Nzc3OGJfSUQ6NzYzMzc2MjUxNzQ4NzYxOTAxNF8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

若抬升，请调低数值。

若下降，请调高数值。

## 7\>原点位置

### 关节轴向及零点位置

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2JhODQyNzQwMDNkOWE3Zjk0YmVhMTI0ZDVlMGM1ODVfMTI4YWMyYTBjYjI0YzZhZTE4ZWJlYjBiYmZhNWQxOWRfSUQ6NzYzMzY3Mjg5NDU5MzY4MjYzMF8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

关节转向符合右手定理，大拇指的指向关节轴向，四指方向就是电机转动的正方向。

此位置为各关节零位。

### 关节范围

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzI1ZTUzYWJhMGRjOTA4ZDBhNGNiYmJjNjFjOTlkYWNfYTkwNzQxZTdhMWMwZGU5Y2Y5MzVlNDE5ZTk4NWViNDVfSUQ6NzYzMzY3MjA2MjI3MTM3NjU3NV8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

### 末端坐标系

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmM5ZWUxYTU0NDgyNmZiZWI3NDJmOWQzZmY2NzY0OWNfMDFhNjVhNThmMTBlM2I0MjJmMzk2ZmJlOGNmYjcxZGRfSUQ6NzYzMzY3MjA2MDYyNzQ4NzY4NV8xNzgxODY2NTAxOjE3ODE5NTI5MDFfVjM)

在初始位置，末端坐标系和参考坐标系重合，位置和姿态都是0，如上图所示。



