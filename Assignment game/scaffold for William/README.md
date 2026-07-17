# Scaffold for William

这是一个给 Python 新手使用的 Acorn Runner 起步 scaffold。它不是完整答案，而是一个清晰的项目骨架：文件已经分好，TODO 已经标出，William 可以每天补一小部分。

## 文件结构

```text
scaffold for William/
├── run.py
├── game.py
├── player.py
├── cells.py
├── game_parser.py
├── grid.py
├── solver.py
├── board_simple.txt
├── board_fire.txt
├── board_teleport.txt
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_grid.py
    └── test_game.py
```

## 如何运行

先进入这个文件夹：

```bash
cd "scaffold for William"
```

运行游戏：

```bash
python3 run.py board_simple.txt
```

运行 solver 占位程序：

```bash
python3 solver.py board_simple.txt BFS
```

## 每天做什么

### 第 1 天：完成 parser

写：

- `cells.py`：已完成基础 Cell 类
- `player.py`：已完成 Player 基础属性
- `game_parser.py`：补完 `parse(lines)`

目标：

```bash
python3 -m tests.test_parser
```

让 parser 测试通过。

### 第 2 天：完成地图显示

写：

- `grid.py` 的 `grid_to_string(grid, player)`
- 确认 `game.py` 可以找到玩家

目标：

```bash
python3 run.py board_simple.txt
python3 -m tests.test_grid
```

应该能看到玩家 `A` 显示在起点位置。

### 第 3 天：完成基础移动

写：

- `game.py` 的 `move_player(move)`

只处理：

- 空地
- 起点
- 终点
- 墙

目标：

```bash
python3 -m tests.test_game
```

手动运行：

```bash
python3 run.py board_simple.txt
```

输入：

```text
d
d
```

玩家应该到达终点。

### 第 4 天：加入水桶和火

写：

- 踩到 `W`：水桶 +1，格子变空地
- 踩到 `F` 且有水：水桶 -1，火变空地
- 踩到 `F` 且无水：游戏失败

运行：

```bash
python3 run.py board_fire.txt
```

输入：

```text
d
d
d
```

### 第 5 天：加入传送门和最终输出

写：

- 传送门成对检查
- 踩到数字传送到另一个相同数字
- 胜利输出
- 失败输出
- `q` 退出

运行：

```bash
python3 run.py board_teleport.txt
```

### 第 6 天：补充自己的测试

扩展：

- `tests/test_parser.py`
- `tests/test_grid.py`
- `tests/test_game.py`

至少覆盖：

- 非法字符
- 没有起点
- 多个起点
- 没有终点
- 撞墙
- 拿水桶
- 灭火
- 传送门不匹配

### 第 7 天：做 solver 和报告

写：

- `solver.py` BFS
- `solver.py` DFS
- report 的 Testing 部分
- report 的 Solver 部分

先让 BFS 在简单地图上工作，再处理水、火、传送门。

## 注意

- `grid_to_string()` 必须 return 字符串，不要直接 print。
- 地图里的空格是有效格子，不要用 `strip()` 删除整行空格。
- `parse()` 需要保留函数名和参数，因为自动测试会直接调用。
- `display` 是属性，不是方法。
- 每天只补当天 TODO，不要一次写完整个游戏。
