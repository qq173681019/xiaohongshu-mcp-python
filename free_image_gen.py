#!/usr/bin/env python3
"""免费图像生成工具 - 使用多个免费API"""

import requests
import json
import base64
import time
from pathlib import Path


def generate_image_huggingface(prompt: str):
    """使用 Hugging Face 免费API生成图片"""
    
    # 使用免费的Stable Diffusion模型
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    
    # 您可以在 https://huggingface.co/settings/tokens 获取免费token
    # 这里使用公共推理端点（有限制但免费）
    headers = {
        "Content-Type": "application/json",
    }
    
    # 将中文提示词翻译为英文（Stable Diffusion对英文效果更好）
    prompt_translations = {
        "一盘精美的中式美食，色彩丰富，摆盘精致": "A beautiful plate of Chinese cuisine, colorful, exquisite presentation, food photography, high quality",
        "春日里的樱花盛开，温暖阳光": "Cherry blossoms blooming in spring, warm sunlight, beautiful landscape, peaceful",
        "现代简约的咖啡厅，温馨舒适": "Modern minimalist coffee shop, cozy and comfortable, interior design, warm lighting",
        "可爱的小猫在阳光下睡觉": "Cute kitten sleeping in sunlight, adorable, peaceful, high quality photography"
    }
    
    english_prompt = prompt_translations.get(prompt, f"high quality, detailed: {prompt}")
    
    data = {
        "inputs": english_prompt,
        "parameters": {
            "num_inference_steps": 20,
            "guidance_scale": 7.5
        }
    }
    
    try:
        print(f"🎨 正在使用 Hugging Face 生成图片...")
        print(f"📝 提示词: {english_prompt}")
        print("⏳ 请稍候...")
        
        response = requests.post(API_URL, headers=headers, json=data, timeout=60)
        
        if response.status_code == 200:
            # 保存图片
            filename = f"generated_image_hf_{int(time.time())}.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ 图片生成成功!")
            print(f"💾 图片已保存为: {filename}")
            return filename
        elif response.status_code == 503:
            print("⏳ 模型正在加载中，请稍后再试...")
            return None
        else:
            print(f"❌ API调用失败: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        return None


def generate_image_pollinations(prompt: str):
    """使用 Pollinations.AI 免费API生成图片"""
    
    try:
        print(f"🎨 正在使用 Pollinations.AI 生成图片...")
        print(f"📝 提示词: {prompt}")
        print("⏳ 请稍候...")
        
        # Pollinations.AI 支持中文，但英文效果更好
        prompt_translations = {
            "一盘精美的中式美食，色彩丰富，摆盘精致": "beautiful Chinese cuisine, colorful, elegant plating, food photography",
            "春日里的樱花盛开，温暖阳光": "cherry blossoms in spring, warm sunlight, beautiful",
            "现代简约的咖啡厅，温馨舒适": "modern minimalist cafe, cozy comfortable interior",
            "可爱的小猫在阳光下睡觉": "cute kitten sleeping in sunlight, adorable peaceful"
        }
        
        english_prompt = prompt_translations.get(prompt, prompt)
        
        # 构建URL (Pollinations.AI 通过GET请求生成图片)
        import urllib.parse
        encoded_prompt = urllib.parse.quote(english_prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
        
        # 下载图片
        response = requests.get(image_url, timeout=60)
        
        if response.status_code == 200:
            # 保存图片
            filename = f"generated_image_poll_{int(time.time())}.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ 图片生成成功!")
            print(f"💾 图片已保存为: {filename}")
            return filename
        else:
            print(f"❌ API调用失败: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        return None


def main():
    """主函数"""
    print("🚀 免费图片生成工具")
    print("="*50)
    print("提示：使用免费服务，生成速度可能较慢")
    print("")
    
    # 预设一些提示词
    prompts = [
        "一盘精美的中式美食，色彩丰富，摆盘精致",
        "春日里的樱花盛开，温暖阳光",
        "现代简约的咖啡厅，温馨舒适",
        "可爱的小猫在阳光下睡觉"
    ]
    
    print("请选择要生成的图片:")
    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. {prompt}")
    print(f"{len(prompts)+1}. 自定义提示词")
    
    print("\n可用的免费服务:")
    print("1. Pollinations.AI (推荐，速度快)")
    print("2. Hugging Face (质量高，可能需要等待)")
    
    try:
        choice = int(input("\n请选择图片内容 (1-5): "))
        
        if 1 <= choice <= len(prompts):
            prompt = prompts[choice-1]
        elif choice == len(prompts)+1:
            prompt = input("请输入自定义提示词: ").strip()
            if not prompt:
                print("❌ 提示词不能为空")
                return
        else:
            print("❌ 无效选择")
            return
        
        service_choice = input("\n选择服务 (1=Pollinations, 2=HuggingFace, 默认1): ").strip()
        
        # 生成图片
        if service_choice == "2":
            result = generate_image_huggingface(prompt)
        else:
            result = generate_image_pollinations(prompt)
        
        if result:
            print(f"\n🎉 成功！图片已生成并保存为 {result}")
            print("📁 图片保存在当前目录下")
        else:
            print("\n❌ 图片生成失败")
            
    except KeyboardInterrupt:
        print("\n👋 已取消")
    except ValueError:
        print("❌ 请输入有效数字")


if __name__ == "__main__":
    main()