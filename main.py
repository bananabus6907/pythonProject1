from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pygame
import random

app = Ursina()

window.fps_counter.enabled = False  #프레임값 안보이게 삭제
window.exit_button.visible = False  #창 닫는 부분 안보이게 삭제

punch = Audio('blocks/assets_punch.wav', autoplay=False) #블럭 부수는 소리 재생, 시작시 자동재생 방지

pygame.mixer.init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
pygame.mixer.music.load('Minecraft.mp3') #마인크래프트 배경음악 재생
pygame.mixer.music.play(-1)



blocks = [  #블럭에 적용할 텍스처값 리스트
    load_texture('blocks/assets_dia.png'),  # 0
    load_texture('blocks/assets_glass.png'),  # 1
    load_texture('blocks/assets_stone.png'),  # 2
    load_texture('blocks/assets_wood.png'),  # 3
    load_texture('blocks/assets_brick.png'),  # 4
    load_texture('blocks/assets_grass.png'),  # 5
    load_texture('blocks/assets_lava.png'),  # 6
    load_texture('blocks/assets_stonebrick.png'),  # 7
    load_texture('blocks/assets_pumpkin.png'),  # 8
    load_texture('blocks/assets_wool.png'),  # 9
]

block_id = 1


def input(key): #블럭 종류와 블럭에 지정된 키 함수
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]


sky = Entity(   #하늘 만들기
    parent=scene,
    model='sphere',
    texture=load_texture('blocks/assets_sky.jpg'),
    scale=500,
    double_sided=True
)

hand = Entity(  #손에 들고 있는 블록 표현하기
    parent=camera.ui,
    model='block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)


class health:   #체력바 표현하기
    health1 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.8, -0.3)
    )

    health2 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.75, -0.3)
    )

    health3 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.7, -0.3)
    )

    health4 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.65, -0.3)
    )

    health5 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.6, -0.3)
    )

    health6 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.55, -0.3)
    )

    health7 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.5, -0.3)
    )

    health8 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.45, -0.3)
    )

    health9 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.4, -0.3)
    )

    health10 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.35, -0.3)
    )


class hunger:   #배고픔바 표현하기
    hunger1 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.8, -0.3)
    )

    hunger2 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.75, -0.3)
    )

    hunger3 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.7, -0.3)
    )

    hunger4 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.65, -0.3)
    )

    hunger5 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.6, -0.3)
    )

    hunger6 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.55, -0.3)
    )

    hunger7 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.5, -0.3)
    )

    hunger8 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.45, -0.3)
    )

    hunger9 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.4, -0.3)
    )

    hunger10 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.35, -0.3)
    )


def update():   #클릭할때 움직이는 모션 표현, 소리 발생
    if held_keys['right mouse'] or held_keys['left mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)


class Voxel(Button):    #초기 맵 초기화 및 설정 1층 잔디를 나타내는 클래스
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):    #클릭 했을 때 블럭 설치, 파괴하는 함수
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)


class Voxel1(Button):    #초기 맵 초기화 및 설정 1층 아래 돌 블럭을 나타내는 클래스
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_stone.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):    #클릭 했을 때 블럭 설치, 파괴하는 함수
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)

class Voxel2(Button):    #초기 맵 초기화 및 설정 1층 아래 돌 블럭 중 일부를 다이아몬드 원석으로 바꾸는 클래스
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_dia.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):    ##클릭 했을 때 블럭 설치, 파괴하는 함수
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)


for z in range(25):    #1층 잔디
    for x in range(25):
        voxel = Voxel(position=(x, 0, z))

for z in range(25):    #1층 아래 돌
    for x in range(25):
        for y in range(-7, 0, 1):
            voxel1 = Voxel1(position=(x, y, z))

for i in range(25):    #1층 아래 돌 중 다이아몬드
    a = random.randrange(1, 21)
    b = random.randrange(-7, 0)
    c = random.randrange(1, 21)
    voxel2 = Voxel2(position=(a, b, c))
player = FirstPersonController()
health()
hunger()
app.run()

