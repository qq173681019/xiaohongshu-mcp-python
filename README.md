# 🚀 AI 社交媒体运营全栈解决方案

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![MCP Protocol](https://img.shields.io/badge/MCP-1.0%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**🤖 AI驱动的智能社交媒体运营平台 | 让AI帮你运营小红书**

[快速开始](#-快速开始) • [项目架构](#-项目架构) • [核心功能](#-核心功能) • [使用指南](#-使用指南)

</div>

---

## ✨ 项目简介

这是一个**完整的AI社交媒体运营解决方案**，由四个强大的项目组成，实现从内容生成、平台操作到AI智能调度的全链路自动化。

### 🎯 核心价值

- **🤖 AI自主运营**：AI模型自主决策和执行运营任务，无需人工干预
- **🔄 事件驱动**：智能响应用户请求、平台通知、定时任务等多种事件
- **📊 数据驱动**：基于数据分析自动优化内容策略和发布时机
- **🔌 模块化设计**：内容生成、平台操作、AI调度三层架构，灵活可扩展
- **🎨 内容创作**：AI自动生成图像和视频，支持完整的内容创作流程
- **📱 多平台支持**：支持小红书、抖音、快手等平台（逐步扩展）

---

## 📖 使用指南

### 场景一：生成内容、图片、并发布于小红书

```
[新对话] 请输入消息: 写个单身程序员如何找富婆的小红书，配9张图，其中有核心图有类似狂飙中大嫂陈舒婷
📤 发送中...
📥 最终生成的小红书
```

**最终发布的小红书：**

![富婆圣经0](assets/富婆圣经0.png)

![富婆圣经1](assets/富婆圣经1.png)

## 🏗️ 项目架构

本仓库包含四个独立但协同工作的项目：

### 1️⃣ **ai_social_scheduler** - AI 调度核心层

**定位**：上层智能调度系统，AI自主决策和执行运营任务

- 🤖 **AI自主驱动**：AI模型分析运营目标，自动生成和执行计划
- 🔄 **事件响应**：支持用户请求、平台通知、定时任务等多种事件
- 📊 **策略优化**：基于数据分析自动调整内容策略
- 🎨 **内容创作**：AI生成内容创作计划，调用底层服务执行
- 📈 **数据分析**：内容表现分析、趋势识别、热点追踪
- 🌐 **HTTP API 服务**：提供 FastAPI 接口，支持 HTTP 调用
- 💬 **交互式聊天**：提供命令行聊天客户端，方便快速体验

**核心文件**：
- **`run.py`**：启动 FastAPI 服务器，提供 HTTP API 接口（默认端口 8012）
- **`chat.py`**：交互式聊天客户端，通过命令行与 AI Agent 对话

**适用场景**：需要AI智能运营和自动化调度的场景

### 2️⃣ **xhs-content-generator-mcp** - 小红书内容生成 MCP 服务层

**定位**：内容文案生成引擎，提供AI内容创作能力

- ✍️ **内容生成**：基于主题生成小红书笔记、标题、描述等内容
- 🎯 **多类型支持**：支持笔记、标题、描述等多种内容类型
- 🚀 **FastMCP框架**：使用 FastMCP 快速构建 MCP 服务
- 🔌 **MCP协议实现**：完整支持 Model Context Protocol 规范
- 🎨 **智能创作**：AI驱动的智能内容创作

**适用场景**：需要AI生成小红书文案和内容的场景

### 3️⃣ **xhs-browser-automation-mcp** - 小红书浏览器自动化 MCP 服务层

**定位**：平台操作引擎，提供小红书平台的具体操作能力

- 🎯 **MCP协议实现**：完整实现 Model Context Protocol 规范
- 🚀 **高性能**：基于 Playwright 的异步浏览器自动化
- 📝 **内容发布**：支持图文、视频内容发布
- 🔍 **内容管理**：搜索、获取、互动等完整功能
- 🔐 **账户管理**：登录、会话保持、自动重连

**适用场景**：需要直接操作小红书平台的场景

### 4️⃣ **image_video_mcp** - 图像视频生成 MCP 服务层

**定位**：内容创作引擎，提供AI图像和视频生成能力

- 🎨 **图像生成**：基于提示词生成高质量图像（支持通义万相）
- 🎬 **视频生成**：基于提示词生成视频内容
- 🚀 **FastMCP框架**：使用 FastMCP 快速构建 MCP 服务
- 🔌 **MCP协议实现**：完整支持 Model Context Protocol 规范
- ⚙️ **灵活配置**：支持自定义尺寸、种子、负面提示词等参数

**适用场景**：需要AI生成图像或视频内容的场景

### 🔗 协同工作

```
┌─────────────────────────────────────────┐
│   AI Social Scheduler (智能调度层)        │
│   - AI决策引擎                           │
│   - 事件监听器                           │
│   - 任务调度器                           │
│   - 策略管理器                           │
└───┬──────────┬──────────┬───────────────┘
    │ MCP协议  │ MCP协议  │ MCP协议
    ↓          ↓          ↓
┌──────────────┐ ┌──────────────┐ ┌────────────────────┐
│xhs-content   │ │image_video_mcp│ │xhs-browser-auto-mcp │
│generator     │ │(图像视频生成) │ │ (平台操作服务层)    │
│              │ │              │ │                    │
│- 内容生成    │ │- 图像生成     │ │- 小红书内容发布    │
│- 文案创作    │ │- 视频生成     │ │- 内容搜索与获取    │
│              │ │              │ │- 用户互动管理      │
└──────────────┘ └──────────────┘ │- 账户管理          │
                                  └────────┬───────────┘
                                       │ 浏览器自动化
                                       ↓
                                 ┌──────────┐
                                 │  小红书平台 │
                                 └──────────┘
```

---

## 🎯 核心功能

### 🤖 AI 智能运营

- **自主决策**：AI分析运营目标，自动生成内容创作计划
- **智能调度**：根据数据表现自动调整发布策略和时机
- **事件响应**：实时响应平台通知、用户请求、定时任务
- **策略优化**：基于历史数据持续优化运营策略

### 🎨 内容生成

- **图像生成**：基于提示词AI生成高质量图像
- **视频生成**：基于提示词AI生成视频内容
- **文案生成**：AI生成小红书笔记、标题、描述等内容
- **参数定制**：支持自定义尺寸、种子、负面提示词等
- **批量生成**：支持批量生成和异步处理

### 📝 内容发布

- **图文发布**：支持多图片、标签、标题和描述
- **视频发布**：支持视频上传、自动等待处理完成
- **批量操作**：支持批量发布和定时发布
- **内容管理**：搜索、获取、编辑内容

### 📊 数据分析

- **表现分析**：阅读量、点赞、评论、转发等数据统计
- **趋势识别**：内容趋势分析和热点识别
- **用户洞察**：粉丝增长、互动率等用户数据
- **策略建议**：基于数据自动生成优化建议

### 🔍 内容管理

- **内容搜索**：关键词搜索小红书内容
- **推荐获取**：获取首页推荐列表
- **详情分析**：获取帖子详情和互动数据
- **用户管理**：获取用户主页信息

---

## 🚀 快速开始

### 📋 环境要求

- **Python >= 3.11**
- **uv 包管理器**（快速安装 Python 依赖）
- **支持的操作系统**：Linux, macOS, Windows
- **通义万相 API Key**（图像生成，[获取地址](https://dashscope.aliyun.com/)）
- **小红书账号**（需要在浏览器中登录）

### 🔧 一键安装与配置

#### 步骤 1：克隆项目

```bash
git clone git@github.com:luyike221/xiaohongshu-mcp-python.git
cd xiaohongshu-mcp-python
```

#### 步骤 2：安装 uv 包管理器

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows PowerShell:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装完成后，重启终端使 `uv` 命令生效。

#### 步骤 3：安装所有项目依赖

**方式一：自动安装所有依赖（推荐）**

在项目根目录运行安装脚本：

**Windows PowerShell:**
```powershell
# 安装所有项目依赖
cd image_video_mcp ; uv sync ; cd ..
cd xhs-content-generator-mcp ; uv sync ; cd ..
cd xhs-browser-automation-mcp ; uv sync ; uv run playwright install chromium ; cd ..
cd ai_social_scheduler ; uv sync ; cd ..
```

**macOS/Linux:**
```bash
# 安装所有项目依赖
cd image_video_mcp && uv sync && cd ..
cd xhs-content-generator-mcp && uv sync && cd ..
cd xhs-browser-automation-mcp && uv sync && uv run playwright install chromium && cd ..
cd ai_social_scheduler && uv sync && cd ..
```

**方式二：逐个安装（可选）**

如果只需要使用部分功能，可以选择性安装：

```bash
# 安装图像视频生成服务（必需）
cd image_video_mcp
uv sync

# 安装小红书内容生成服务（必需）
cd xhs-content-generator-mcp
uv sync

# 安装小红书浏览器自动化服务（必需）
cd xhs-browser-automation-mcp
uv sync
uv run playwright install chromium

# 安装 AI 调度系统（推荐）
cd ai_social_scheduler
uv sync
```

#### 步骤 4：配置 API Keys 和环境变量

**4.1 配置图像视频生成服务**

在 `image_video_mcp` 目录下创建 `.env` 文件：

```env
# 服务器配置
MCP_HOST=127.0.0.1
MCP_PORT=8003

# 通义万相 API 配置（必需）
# 获取地址：https://dashscope.aliyun.com/
WANT2I_API_KEY=sk-your-api-key-here
WANT2I_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

**4.2 配置小红书浏览器自动化服务**

在 `xhs-browser-automation-mcp` 目录下创建 `.env` 文件：

```env
# 环境模式: development（开发）或 production（生产）
ENV=development

# 服务器配置
SERVER_HOST=127.0.0.1
SERVER_PORT=8000

# 默认用户名（可选，用于多账号管理）
GLOBAL_USER=default_user
```

**4.3 配置 AI 调度系统（可选）**

AI 调度系统可以使用默认配置，如需自定义：

```bash
cd ai_social_scheduler
# 复制示例配置文件（如果存在）
# cp config/config.example.yaml config/config.yaml
# 编辑 config/config.yaml 填入实际配置
```

#### 步骤 5：一键启动所有服务

**Windows PowerShell（推荐使用提供的启动脚本）:**

项目根目录下提供了便捷启动脚本：

```powershell
# 使用便捷启动脚本
python start_xiaohongshu_automation.py
```

或手动启动（在不同的 PowerShell 窗口中）：

```powershell
# 窗口 1：启动图像生成服务
cd image_video_mcp
uv run python -m image_video_mcp.main

# 窗口 2：启动浏览器自动化服务
cd xhs-browser-automation-mcp
uv run python -m xiaohongshu_mcp_python.main

# 窗口 3：启动内容生成服务（可选）
cd xhs-content-generator-mcp
uv run python -m xhs_content_generator_mcp.main
```

**macOS/Linux:**

```bash
# 使用便捷启动脚本
python3 start_xiaohongshu_automation.py
```

或手动启动（在不同的终端窗口中）：

```bash
# 终端 1：启动图像生成服务
cd image_video_mcp
uv run python -m image_video_mcp.main

# 终端 2：启动浏览器自动化服务
cd xhs-browser-automation-mcp
uv run python -m xiaohongshu_mcp_python.main

# 终端 3：启动内容生成服务（可选）
cd xhs-content-generator-mcp
uv run python -m xhs_content_generator_mcp.main
```

#### 步骤 6：登录小红书账号

服务启动后，浏览器自动化服务会自动打开浏览器窗口：

1. **首次使用**：浏览器会打开小红书登录页面
2. **手动登录**：使用你的小红书账号登录（扫码或密码登录均可）
3. **保持登录**：登录成功后，系统会自动保存 Cookie，下次启动无需重新登录
4. **验证登录**：看到浏览器标题显示"小红书"且能正常访问，说明登录成功

> 💡 **提示**：登录信息会保存在 `xhs-browser-automation-mcp/storage/cookies/` 目录下，请妥善保管。

#### 步骤 7：验证服务状态

打开浏览器访问以下地址，确认服务正常运行：

- **图像生成服务**: http://localhost:8003
- **浏览器自动化服务**: http://localhost:8000
- **内容生成服务**: http://localhost:8001（如果启动了）

看到服务响应说明启动成功！

---

### 🎯 三种使用方式

#### 方式一：使用便捷脚本（最简单，推荐新手）

项目根目录提供了简单易用的 Python 脚本：

```bash
# 使用自动化启动脚本（已包含服务启动）
python start_xiaohongshu_automation.py

# 或使用免费图像生成脚本
python free_image_gen.py
```

这些脚本会自动：
- 检查服务状态
- 启动所需服务
- 提供友好的交互界面

#### 方式二：使用交互式命令行（灵活，适合快速测试）

启动 AI 调度系统的交互式客户端：

```bash
cd ai_social_scheduler
uv run python chat.py
```

然后直接与 AI 对话：

```
[新对话] 请输入消息: 写一篇关于咖啡的小红书，配3张图

AI 会自动：
1. 生成小红书文案
2. 调用图像生成服务创建3张配图
3. 打开浏览器发布到小红书
4. 返回发布结果
```

支持的命令：
- 输入任何消息：与 AI 对话，让 AI 帮你完成任务
- `quit` 或 `exit`：退出程序
- `reset`：重置对话，开始新的话题

#### 方式三：通过 HTTP API 调用（高级，适合集成）

启动 HTTP API 服务：

```bash
cd ai_social_scheduler
uv run python run.py
```

服务将在 `http://localhost:8012` 启动。

使用 curl 或其他工具调用：

```bash
# 发送聊天消息
curl -X POST http://localhost:8012/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "写一篇关于咖啡的小红书，配3张图",
    "thread_id": null
  }'

# 返回示例
{
  "thread_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "response": "好的，我来帮你创建一篇关于咖啡的小红书...",
  "message_count": 2
}
```

---

### 💡 常见问题与解决

#### Q1: 服务启动失败，提示端口被占用？

**解决方法：**
```bash
# Windows 查看端口占用
netstat -ano | findstr "8000"
netstat -ano | findstr "8003"

# 结束占用端口的进程
taskkill /PID <进程ID> /F

# Linux/macOS 查看端口占用
lsof -i :8000
lsof -i :8003

# 结束占用端口的进程
kill -9 <进程ID>
```

或修改 `.env` 文件中的端口配置。

#### Q2: Playwright 安装失败或浏览器无法启动？

**解决方法：**
```bash
# 重新安装 Playwright 浏览器
cd xhs-browser-automation-mcp
uv run playwright install chromium --with-deps

# 如果仍然失败，尝试安装完整版
uv run playwright install --with-deps
```

#### Q3: 图像生成失败，提示 API Key 错误？

**解决方法：**
1. 检查 `image_video_mcp/.env` 文件中的 `WANT2I_API_KEY` 是否正确
2. 访问 https://dashscope.aliyun.com/ 确认 API Key 有效且有余额
3. 确认 API Key 权限包含图像生成功能

#### Q4: 小红书登录后提示 Cookie 过期？

**解决方法：**
1. 删除旧的 Cookie 文件：
   ```bash
   # Windows
   del xhs-browser-automation-mcp\storage\cookies\*.json
   
   # Linux/macOS
   rm xhs-browser-automation-mcp/storage/cookies/*.json
   ```
2. 重启服务，重新登录

#### Q5: 如何只使用部分功能（比如只生成图片）？

**解决方法：**

如果只需要图像生成功能：

```bash
# 只启动图像生成服务
cd image_video_mcp
uv run python -m image_video_mcp.main

# 使用免费图像生成脚本
python free_image_gen.py
```

如果只需要发布内容（不生成图片）：

```bash
# 只启动浏览器自动化服务
cd xhs-browser-automation-mcp
uv run python -m xiaohongshu_mcp_python.main

# 手动调用 MCP 工具发布内容
```

---

### 🎓 使用教程视频

> 📹 **即将推出**：完整的视频教程，从安装到发布第一篇小红书

---

## 📖 完整使用指南

### 📝 场景一：AI 全自动生成并发布小红书（最简单）

这是**最推荐的使用方式**，只需要一句话，AI 会自动完成所有工作。

#### 使用步骤：

1. **启动服务**（使用便捷脚本）

```bash
# 在项目根目录运行
python start_xiaohongshu_automation.py
```

脚本会自动启动所有必需的服务（图像生成 + 浏览器自动化）。

2. **与 AI 对话**

启动交互式聊天客户端：

```bash
cd ai_social_scheduler
uv run python chat.py
```

3. **输入你的需求**

```
[新对话] 请输入消息: 写一篇关于手冲咖啡的小红书，配3张精美的咖啡图片

📤 发送中...
📥 AI 回复:
好的！我来帮你创建一篇关于手冲咖啡的小红书笔记...

正在生成内容文案...
正在生成第1张图片：手冲咖啡器具特写...
正在生成第2张图片：咖啡豆研磨过程...
正在生成第3张图片：成品咖啡...
正在发布到小红书...

✅ 发布成功！
```

**AI 会自动完成**：
1. ✅ 生成吸引人的小红书文案
2. ✅ 创建 3 张高质量的咖啡主题图片
3. ✅ 添加合适的标签和话题
4. ✅ 自动打开浏览器发布到小红书
5. ✅ 返回发布结果和链接

#### 更多示例：

```bash
# 美食类
写一篇关于火锅的小红书，配5张图

# 旅游类  
写一篇关于杭州西湖的旅游攻略，配6张美景图

# 时尚类
写一篇秋冬穿搭指南，配4张穿搭图片

# 美妆类
写一篇新手化妆教程，配图展示化妆步骤

# 生活方式
分享一个早起的好处，配3张清晨阳光图
```

---

### 🎨 场景二：只生成图片（不发布）

如果你只想生成图片，不想发布到小红书：

#### 使用方式一：使用免费图像生成脚本

```bash
# 在项目根目录运行
python free_image_gen.py
```

按照提示输入你想生成的图片描述：

```
请输入图片描述: 一杯冒着热气的手冲咖啡，旁边是咖啡豆和器具

正在生成图片...
✅ 图片已保存到: test_image_1234567890.jpg
```

#### 使用方式二：通过 MCP 客户端调用

如果你使用支持 MCP 的 AI 工具（如 Cursor、Claude Desktop）：

```python
# 调用图像生成工具
generate_image(
    prompt="一杯精美的手冲咖啡",
    n=1,
    size="1024x1024",
    style="<auto>"
)
```

---

### 📱 场景三：手动发布内容到小红书

如果你已有文案和图片，想直接发布到小红书：

#### 步骤 1：准备素材

```
标题：手冲咖啡的正确打开方式
内容：分享我的手冲咖啡心得...
图片：/path/to/image1.jpg, /path/to/image2.jpg
标签：咖啡, 手冲咖啡, 生活方式
```

#### 步骤 2：启动浏览器自动化服务

```bash
cd xhs-browser-automation-mcp
uv run python -m xiaohongshu_mcp_python.main
```

#### 步骤 3：调用发布工具

通过 MCP 客户端或 HTTP API 调用：

```python
# MCP 工具调用
xiaohongshu_publish_content(
    title="手冲咖啡的正确打开方式",
    content="分享我的手冲咖啡心得...",
    images=["/path/to/image1.jpg", "/path/to/image2.jpg"],
    tags=["咖啡", "手冲咖啡", "生活方式"]
)
```

---

### 🔍 场景四：搜索和获取小红书内容

如果你想搜索小红书内容或获取某个笔记的详情：

#### 搜索小红书内容

```python
# MCP 工具调用
xiaohongshu_search_notes(
    keyword="手冲咖啡",
    page=1,
    page_size=20,
    sort_type="general"  # general: 综合排序, time_descending: 最新
)
```

#### 获取笔记详情

```python
# MCP 工具调用
xiaohongshu_get_note_detail(
    note_id="笔记ID"
)
```

#### 获取首页推荐

```python
# MCP 工具调用
xiaohongshu_get_home_feed(
    page_size=20
)
```

---

### 🚀 场景五：批量发布和定时发布（高级）

如果你需要批量发布多篇小红书或定时发布：

#### 批量发布

```bash
# 启动 AI 调度系统
cd ai_social_scheduler
uv run python chat.py
```

然后输入：

```
[新对话] 请输入消息: 帮我创建5篇关于健康生活的小红书，主题分别是：早起、运动、饮食、睡眠、心态

AI 会自动：
1. 为每个主题生成文案
2. 为每篇内容生成配图
3. 依次发布到小红书
4. 返回所有发布结果
```

#### 定时发布（即将支持）

```
[新对话] 请输入消息: 每天早上9点自动发布一篇励志内容

AI 会：
1. 创建定时任务
2. 每天定时生成和发布内容
3. 根据数据反馈优化策略
```

---

### 🔄 场景六：内容管理和互动

#### 获取我的笔记列表

```python
# MCP 工具调用
xiaohongshu_get_user_notes(
    user_id="你的用户ID",
    page=1
)
```

#### 点赞笔记

```python
# MCP 工具调用
xiaohongshu_like_note(
    note_id="笔记ID"
)
```

#### 评论笔记

```python
# MCP 工具调用
xiaohongshu_comment_note(
    note_id="笔记ID",
    content="很棒的分享！"
)
```

---

### 📊 场景七：数据分析和优化（即将支持）

```
[新对话] 请输入消息: 分析我最近发布的10篇笔记，给出优化建议

AI 会：
1. 获取你最近的笔记数据
2. 分析阅读量、点赞、评论等数据
3. 识别热门内容类型和最佳发布时间
4. 给出内容优化建议
```

---

### 🛠️ 场景八：自定义 AI 工作流（高级）

如果你想自定义 AI 的工作流程：

```bash
# 编辑 AI 调度系统配置
cd ai_social_scheduler
# 编辑 config/config.yaml 或 src/ai_social_scheduler/workflows/
```

你可以自定义：
- 内容生成策略
- 图片生成风格
- 发布时机
- 互动规则
- 数据分析方式

---

### 💡 使用技巧和最佳实践

#### 技巧 1：优化图片生成效果

在提示词中使用更详细的描述：

```
❌ 不好的提示词：咖啡
✅ 好的提示词：一杯冒着热气的手冲咖啡，放在木质桌面上，旁边有咖啡豆和手冲壶，温暖的光线，专业摄影
```

#### 技巧 2：提高内容质量

让 AI 生成更具体的内容：

```
❌ 简单请求：写一篇咖啡的小红书
✅ 详细请求：写一篇手冲咖啡的新手教程，包括器具选择、水温控制、冲泡技巧，语气要轻松有趣，配3张步骤图
```

#### 技巧 3：避免账号风险

- 不要短时间内发布过多内容（建议每天不超过 5 篇）
- 适当添加人工互动，不要完全自动化
- 定期检查账号状态
- 遵守平台规则，不发布违规内容

#### 技巧 4：保持登录状态

- 登录成功后，Cookie 会自动保存
- 如果提示登录过期，删除 `xhs-browser-automation-mcp/storage/cookies/` 下的文件，重新登录
- 不要在多个地方同时登录同一账号

#### 技巧 5：批量操作

使用 AI 调度系统可以轻松实现批量操作：

```
请创建一周的小红书内容，主题是健康生活，每天一篇，内容要有关联性

AI 会：
1. 规划一周的内容主题
2. 生成7篇关联的内容
3. 为每篇生成合适的配图
4. 可以选择立即发布或定时发布
```

---

### 🎯 完整工作流示例

一个完整的使用流程：

```bash
# 1. 启动所有服务
python start_xiaohongshu_automation.py

# 2. 启动 AI 聊天客户端
cd ai_social_scheduler
uv run python chat.py

# 3. 与 AI 对话
[新对话] 请输入消息: 我想分享一个关于早起的生活方式内容

📤 AI: 好的！让我帮你创建一篇关于早起的小红书内容。你希望：
1. 重点分享早起的好处
2. 分享你的早起习惯
3. 给出早起的实用技巧

你想要哪个方向？或者我可以综合这些方面来创作。

[对话继续] 请输入消息: 综合这些方面，语气要亲切，配3张清晨阳光的图片

📤 AI: 明白了！我会创作一篇温馨亲切的早起分享，配上3张清晨阳光的图片...

正在生成内容...
✅ 标题：「早起30天后，我的生活发生了这些变化...」
✅ 正在生成配图1：清晨第一缕阳光...
✅ 正在生成配图2：早餐和笔记本...
✅ 正在生成配图3：伸展的身影...
✅ 正在发布到小红书...

🎉 发布成功！
📊 预计阅读量：500+
🔗 笔记链接：https://www.xiaohongshu.com/...

[对话继续] 请输入消息: 太好了！明天帮我发一篇关于运动的

📤 AI: 好的！我已经安排了明天早上9点发布一篇关于运动的内容...
```

这就是完整的使用流程！

---

## 🛠️ 技术栈

### 核心技术

- **Python 3.11+**：主要开发语言
- **uv**：现代 Python 包管理工具
- **MCP 协议**：服务间通信标准
- **LangGraph**：AI Agent 框架
- **Playwright**：浏览器自动化
- **FastAPI**：Web 服务框架

### 数据存储

- **SQLite/PostgreSQL**：关系型数据存储
- **Redis**：缓存和任务队列
- **pgvector**：向量数据库（用于AI功能）

---

## 📁 项目结构

```
.
├── image_video_mcp/                # 图像视频生成 MCP 服务
│   ├── src/
│   │   └── image_video_mcp/
│   │       ├── main.py            # 主程序入口
│   │       ├── clients/           # 客户端模块
│   │       ├── prompts/           # Prompt 模板
│   │       ├── resources/         # Resource 资源
│   │       └── ...
│   └── README.md                  # 详细文档
│
├── xhs-content-generator-mcp/      # 小红书内容生成 MCP 服务
│   ├── src/
│   │   └── xhs_content_generator_mcp/
│   │       ├── __init__.py
│   │       └── main.py           # 主程序入口
│   ├── pyproject.toml
│   └── README.md                  # 详细文档
│
├── xhs-browser-automation-mcp/     # 小红书浏览器自动化 MCP 服务
│   ├── src/
│   │   └── xiaohongshu_mcp_python/
│   │       ├── main.py            # 主程序入口
│   │       ├── server/            # MCP 服务器
│   │       ├── xiaohongshu/       # 小红书操作模块
│   │       └── ...
│   ├── tests/                     # 测试文件
│   └── README.md                  # 详细文档
│
├── ai_social_scheduler/            # AI 调度系统
│   ├── src/
│   │   └── ai_social_scheduler/
│   │       ├── core/              # AI调度核心层
│   │       │   ├── ai_engine.py  # AI决策引擎
│   │       │   ├── event_listener.py # 事件监听器
│   │       │   └── ...
│   │       ├── api/               # FastAPI 接口层
│   │       │   ├── app.py        # FastAPI 应用
│   │       │   └── ...
│   │       ├── mcp/               # MCP服务层
│   │       └── ...
│   ├── run.py                      # 启动 FastAPI 服务器
│   ├── chat.py                     # 交互式聊天客户端
│   ├── config/                     # 配置文件
│   └── README.md                   # 详细文档
│
└── README.md                       # 本文件
```

---

## 🔌 MCP 客户端接入

### Cursor IDE

在项目根目录创建 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "image-video-mcp": {
      "url": "http://localhost:8003",
      "description": "图像视频生成 MCP 服务"
    },
    "xhs-content-generator-mcp": {
      "url": "http://localhost:8001",
      "description": "小红书内容生成 MCP 服务"
    },
    "xhs-browser-automation-mcp": {
      "url": "http://localhost:8000",
      "description": "小红书浏览器自动化 MCP 服务"
    }
  }
}
```

### Claude Desktop

在配置文件中添加：

```json
{
  "mcpServers": {
    "image-video-mcp": {
      "url": "http://localhost:8003"
    },
    "xhs-content-generator-mcp": {
      "url": "http://localhost:8001"
    },
    "xhs-browser-automation-mcp": {
      "url": "http://localhost:8000"
    }
  }
}
```

---

## 🎨 功能演示

### AI 自主运营示例

```python
# 用户请求："帮我写一篇关于美食的小红书"
# 
# AI 调度系统处理流程：
# 1. 事件监听器接收用户请求
# 2. AI 引擎分析需求，生成内容计划：
#    - 主题：美食
#    - 内容方向：分享一道家常菜
#    - 图片需求：需要3张图片
#    - 标签：美食、家常菜、生活
# 3. 任务调度器调用 MCP 服务：
#    - 生成内容（调用 xhs-content-generator-mcp）
#    - 生成图片（调用 image_video_mcp）
#    - 发布内容（调用 xhs-browser-automation-mcp）
# 4. 监控发布结果
# 5. 根据数据调整后续策略
```

### 定时任务示例

```python
# 设置定时任务："每天下午3点发布一篇内容"
# 
# AI 调度系统会：
# 1. 定时触发任务
# 2. AI 分析当天热点和用户偏好
# 3. 生成合适的内容
# 4. 自动发布
# 5. 收集数据并优化策略
```

### 交互式聊天使用示例

使用 `chat.py` 与 AI Agent 进行对话：

```bash
$ cd ai_social_scheduler
$ uv run python chat.py

============================================================
小红书运营 Agent 交互式聊天
============================================================

提示:
  - 输入消息后按 Enter 发送
  - 输入 'quit' 或 'exit' 退出
  - 输入 'reset' 重置对话

[新对话] 请输入消息: 帮我写一篇关于春日美食的小红书

📤 发送中...

📥 AI 回复:
好的，我来帮你创建一篇关于春日美食的小红书内容。让我先分析一下需求...

[对话 ID: a1b2c3d4...] 请输入消息: 标题要吸引人一点

📤 发送中...

📥 AI 回复:
好的，我会优化标题，让它更加吸引人...

消息数: 4

[对话 ID: a1b2c3d4...] 请输入消息: reset
✅ 对话已重置

[新对话] 请输入消息: quit
再见！
```

### HTTP API 使用示例

使用 `run.py` 启动服务后，可以通过 HTTP 调用：

```bash
# 启动服务
$ cd ai_social_scheduler
$ uv run python run.py
INFO:     Started server process [12345]
INFO:     Uvicorn running on http://0.0.0.0:8012

# 在另一个终端发送请求
$ curl -X POST http://localhost:8012/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "帮我写一篇关于春日美食的小红书",
    "thread_id": null
  }'

{
  "thread_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "response": "好的，我来帮你创建一篇关于春日美食的小红书内容...",
  "message_count": 2
}

# 继续对话（使用相同的 thread_id）
$ curl -X POST http://localhost:8012/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "标题要吸引人一点",
    "thread_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  }'
```

---

## ⚠️ 重要注意事项

### 🔒 账户安全

#### 登录管理
- ✅ **首次登录**：服务启动后会自动打开浏览器，手动扫码或密码登录
- ✅ **保持登录**：登录信息会自动保存，下次启动无需重新登录
- ❌ **避免冲突**：不要在多个浏览器或设备上同时登录同一账号
- 🔄 **定期检查**：如果提示登录过期，删除 Cookie 文件重新登录
- 🛡️ **专用账号**：建议使用专门的账号进行自动化操作，不要用主账号

#### Cookie 存储位置
```
xhs-browser-automation-mcp/storage/cookies/
├── default_user.json    # 默认用户的登录信息
└── other_user.json      # 其他用户的登录信息
```

**如何重新登录：**
```bash
# Windows
del xhs-browser-automation-mcp\storage\cookies\*.json

# Linux/macOS
rm xhs-browser-automation-mcp/storage/cookies/*.json

# 然后重启服务，会自动打开登录页面
```

---

### 📊 使用限制和风险

#### 发布频率限制（重要！）

为了避免被平台检测和限制，请注意：

| 时间范围 | 建议发布数量 | 风险等级 |
|---------|-------------|---------|
| 每小时 | ≤ 2 篇 | ✅ 安全 |
| 每天 | ≤ 5 篇 | ✅ 安全 |
| 每天 | 6-10 篇 | ⚠️ 中等风险 |
| 每天 | > 10 篇 | ❌ 高风险 |

**最佳实践：**
- 每篇内容发布间隔至少 30 分钟
- 不要在深夜（0-6点）频繁发布
- 模拟人工操作，添加适当的随机延迟
- 定期进行人工互动（点赞、评论、关注）

#### 内容质量要求

小红书对内容质量有严格要求：

❌ **禁止发布**：
- 违法违规内容
- 虚假广告和欺诈信息
- 侵权内容（盗图、抄袭）
- 低质量和重复内容
- 诱导互动的内容

✅ **推荐发布**：
- 原创优质内容
- 真实的使用体验
- 有价值的知识分享
- 精美的图片和排版

#### 账号风险等级

| 行为 | 风险等级 | 可能后果 |
|------|---------|---------|
| 合理使用，遵守规则 | ✅ 低风险 | 正常运营 |
| 发布频率过高 | ⚠️ 中风险 | 限流、降权 |
| 发布低质量内容 | ⚠️ 中风险 | 内容不推荐 |
| 违规内容 | ❌ 高风险 | 删除内容、封禁账号 |
| 恶意操作 | ❌ 高风险 | 永久封禁 |

---

### 🛡️ 法律和道德声明

#### 使用声明

本项目仅供**学习和研究**使用，使用者需要：

1. **遵守法律法规**：
   - 遵守《中华人民共和国网络安全法》
   - 遵守《互联网信息服务管理办法》
   - 遵守相关数据保护和隐私法规

2. **遵守平台规则**：
   - 遵守小红书平台用户协议
   - 遵守小红书社区公约
   - 不进行恶意操作和违规行为

3. **承担责任**：
   - 使用本工具产生的任何后果由使用者自行承担
   - 因违规使用导致的账号封禁、法律责任等，与本项目无关

#### 禁止行为

**严禁使用本工具进行以下行为：**

❌ 批量注册账号和恶意营销  
❌ 发布虚假信息和诈骗内容  
❌ 侵犯他人知识产权和隐私  
❌ 进行网络攻击和恶意操作  
❌ 其他违法违规行为  

#### 免责声明

- 本项目代码开源，仅供技术学习和研究
- 项目作者不对使用者的任何违规行为负责
- 使用本项目即表示同意上述声明

---

### 🔧 故障排除指南

#### 问题 1：服务启动失败

**症状**：运行启动命令后，服务无法启动或立即退出

**可能原因**：
- Python 版本不符合要求（< 3.11）
- 依赖包未正确安装
- 端口被占用
- 配置文件错误

**解决方法**：

```bash
# 1. 检查 Python 版本
python --version  # 应该是 3.11 或更高

# 2. 重新安装依赖
cd <project_directory>
uv sync

# 3. 检查端口占用（Windows）
netstat -ano | findstr "8000"
netstat -ano | findstr "8003"

# 结束占用的进程
taskkill /PID <进程ID> /F

# 4. 检查配置文件
# 确保 .env 文件存在且配置正确
```

#### 问题 2：图片生成失败

**症状**：图片生成时报错或生成的图片质量很差

**可能原因**：
- API Key 无效或余额不足
- 提示词不符合要求
- 网络连接问题

**解决方法**：

```bash
# 1. 验证 API Key
# 登录 https://dashscope.aliyun.com/
# 检查 API Key 状态和余额

# 2. 检查 .env 配置
cd image_video_mcp
cat .env  # Linux/macOS
type .env  # Windows

# 确保包含正确的配置
WANT2I_API_KEY=sk-your-key-here

# 3. 测试图片生成
python free_image_gen.py

# 4. 优化提示词
# 使用更详细和具体的描述
```

#### 问题 3：浏览器无法启动

**症状**：浏览器自动化服务启动后，浏览器无法打开或立即崩溃

**可能原因**：
- Playwright 浏览器未正确安装
- 系统缺少必要的依赖
- 防火墙或安全软件阻止

**解决方法**：

```bash
# 1. 重新安装 Playwright 浏览器
cd xhs-browser-automation-mcp
uv run playwright install chromium --with-deps

# 2. 检查浏览器是否安装成功
uv run playwright install --help

# 3. Windows 用户可能需要安装 Visual C++ 运行库
# 下载地址：https://aka.ms/vs/17/release/vc_redist.x64.exe

# 4. Linux 用户可能需要安装系统依赖
sudo apt-get install -y \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libxcomposite1 libxdamage1
```

#### 问题 4：发布内容失败

**症状**：内容生成成功，但发布到小红书时失败

**可能原因**：
- 未登录或登录过期
- 图片格式或大小不符合要求
- 内容包含敏感词
- 网络连接问题

**解决方法**：

```bash
# 1. 检查登录状态
# 重新启动浏览器自动化服务，检查是否需要登录

# 2. 检查图片
# 确保图片格式为 JPG/PNG，大小不超过 10MB

# 3. 检查内容
# 避免使用敏感词，检查内容是否符合平台规则

# 4. 重新登录
# 删除 Cookie 文件，重新登录
del xhs-browser-automation-mcp\storage\cookies\*.json
```

#### 问题 5：AI 响应缓慢或无响应

**症状**：发送消息后，AI 长时间无响应或响应很慢

**可能原因**：
- 后台服务未启动
- 网络连接问题
- 生成图片时间较长
- 系统资源不足

**解决方法**：

```bash
# 1. 检查服务状态
# 确保所有必需的服务都已启动
python start_xiaohongshu_automation.py

# 2. 查看服务日志
# 检查各个服务的终端输出，查找错误信息

# 3. 耐心等待
# 图片生成可能需要 10-30 秒
# 完整流程可能需要 1-2 分钟

# 4. 检查系统资源
# 确保系统有足够的内存和 CPU
```

---

### 📞 获取帮助

如果遇到问题无法解决：

1. **查看文档**：仔细阅读本 README 和各子项目的 README
2. **查看日志**：检查终端输出的错误信息
3. **搜索 Issues**：在 GitHub 上搜索类似问题
4. **提交 Issue**：如果是新问题，提交详细的问题报告

**提交 Issue 时请包含**：
- 操作系统和版本
- Python 版本
- 完整的错误信息
- 复现步骤
- 相关配置（隐藏敏感信息）

---

### ✅ 安全使用检查清单

在开始使用前，请确认：

- [ ] 我已阅读并理解所有注意事项
- [ ] 我已配置正确的 API Key
- [ ] 我使用的是专门的测试账号
- [ ] 我了解发布频率限制
- [ ] 我承诺遵守平台规则和法律法规
- [ ] 我知道如何处理常见问题
- [ ] 我已备份重要数据（如有）
- [ ] 我理解使用本工具的风险和责任

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 提交 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证。

---

## 🙏 致谢

- [Model Context Protocol](https://modelcontextprotocol.io) - MCP 协议标准
- [Playwright](https://playwright.dev) - 浏览器自动化工具
- [uv](https://github.com/astral-sh/uv) - 现代 Python 包管理工具
- [LangGraph](https://github.com/langchain-ai/langgraph) - AI Agent 框架

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给它一个 Star！**

Made with ❤️ by [luyike221](https://github.com/luyike221)

</div>

