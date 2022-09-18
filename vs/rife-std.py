### rife v4 倍帧，默认以质量交换性能

import vapoursynth as vs
from vapoursynth import core

colorlv = video_in.get_frame(0).props._ColorRange

# 场景切换的检测阈值，初始设置保守，设置为 0.2 可获得更明显的效果但引入更多瑕疵
scene_th = 0.1
# 使用的显卡序号，0为排序一号
GPU = 0
# 使用的显卡线程数
GPU_t = 2
# 静止帧的检测阈值，不对该类帧进行补偿计算
static_th = 60.0

target_fps = display_fps * 1000
original_fps = container_fps * 1000

if container_fps > 58:
    raise Warning("源帧率超过限制的范围，已临时禁用该脚本。")

prepare = core.misc.SCDetect(clip=video_in, threshold=scene_th)

cut = prepare.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")
cut = core.rife.RIFE(clip=cut,
                     model=9,
                     factor_num=FPS_num,
                     factor_den=FPS_den,
                     gpu_id=GPU,
                     gpu_thread=GPU_t,
                     sc=True,
                     skip=True,
                     skip_threshold=60.0)

output = cut.resize.Bilinear(format=video_in.format.id, matrix_s="709", range=1 if colorlv == 0 else None)

output.set_output()
