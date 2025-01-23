# 代理库源代码生成器

🌍 **[English](README.md) | [简体中文](README-CN.md)**

一个用于生成动态链接库（DLL）的代理库源代码的脚本，主要用于实现对原动态链接库的劫持或对目标程序的注入。

## 使用方法

```text
python3 generate_proxy_pe_source.py <options_list>
```

### 选项列表

- `-f, --original-pe-file`
    - 原始 PE 文件路径（必填）

- `-s, --pe-file-path-in-source-file`
    - 生成的源文件中 PE 文件的路径，用于在目标系统中找到相应的 PE 文件
    - 默认值：与 `-f, --original-pe-file` 相同

- `-o, --output-directory`
    - 源代码输出目录
    - 默认值：当前目录

- `-e, --encoding`
    - 生成的源代码编码
    - 默认值：UTF-8

- `-h, --help`
    - 显示帮助信息

## 使用示例

> 更详细的使用示例可参考 [WPSProfileVerificationPatch](https://github.com/YukiIsait/WPSProfileVerificationPatch) 项目。

1. 安装 Python 3.x 环境，并安装依赖库：

```powershell
pip3 install -r requirements.txt
```

2. 生成一个 64 位 `ncrypt.dll` 的代理库源代码：

```powershell
python3 generate_proxy_pe_source.py -f $env:SystemRoot\System32\ncrypt.dll -s %SystemRoot%\System32\ncrypt.dll -o ncrypt64
```

3. 生成一个 32 位 `ncrypt.dll` 的代理库源代码：

```powershell
python3 generate_proxy_pe_source.py -f $env:SystemRoot\SysWOW64\ncrypt.dll -s %SystemRoot%\System32\ncrypt.dll -o ncrypt32
```

4. 将生成的源代码文件添加到基于 MSBuild 的 DLL 项目中，由于不同架构的 `ncrypt.dll` 导出定义相同，可以将 `ProxyLibraryExports.asm` 文件重命名为 64 位和 32 位版本并设置条件编译。

5. 添加 **MASM** 目标后添加生成的 ASM 文件并将其类型设置为 **Microsoft Macro Assembler**。

6. 添加生成的 DEF 文件并将其设置为链接器的 **Module Definition File**。

7. 引用 `ProxyLibrary.h` 头文件并在 `DllMain` 的 `DLL_PROCESS_ATTACH` 中调用 `ProxyLibrary_Load`，在 `DLL_PROCESS_DETACH` 中调用 `ProxyLibrary_Unload`。

8. 编译项目即可生成用于 Hook 的代理 DLL 文件。

## 许可证

此项目根据 MIT 许可证授权，详见 [LICENSE](LICENSE.md) 文件。
