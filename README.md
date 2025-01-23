# Proxy Library Source Code Generator

🌍 **[简体中文](README-CN.md) | [English](README.md)**

A script for generating proxy library source code for dynamic link libraries (DLL), mainly used for hijacking the original dynamic link library or injecting into the target program.

## Usage

```text
python3 generate_proxy_pe_source.py <options_list>
```

### Options List

- `-f, --original-pe-file`
    - Path to the original PE file (required)

- `-s, --pe-file-path-in-source-file`
    - Path to the PE file in the generated source file, used to locate the corresponding PE file on the target system
    - Default: same as `-f, --original-pe-file`

- `-o, --output-directory`
    - Output directory for the source code
    - Default: current directory

- `-e, --encoding`
    - Encoding for the generated source code
    - Default: UTF-8

- `-h, --help`
    - Show help message

## Usage Examples

> For more detailed usage examples, refer to the [WPSProfileVerificationPatch](https://github.com/YukiIsait/WPSProfileVerificationPatch) project.

1. Install Python 3.x environment and install dependencies:

```powershell
pip3 install -r requirements.txt
```

2. Generate proxy library source code for a 64-bit `ncrypt.dll`:

```powershell
python3 generate_proxy_pe_source.py -f $env:SystemRoot\System32\ncrypt.dll -s %SystemRoot%\System32\ncrypt.dll -o ncrypt64
```

3. Generate proxy library source code for a 32-bit `ncrypt.dll`:

```powershell
python3 generate_proxy_pe_source.py -f $env:SystemRoot\SysWOW64\ncrypt.dll -s %SystemRoot%\System32\ncrypt.dll -o ncrypt32
```

4. Add the generated source code files to an MSBuild-based DLL project. Since the export definitions of `ncrypt.dll` are the same for different architectures, you can rename the `ProxyLibraryExports.asm` file for 64-bit and 32-bit versions and set conditional compilation.

5. Add the **MASM** target, then add the generated ASM file and set its type to **Microsoft Macro Assembler**.

6. Add the generated DEF file and set it as the **Module Definition File** for the linker.

7. Include the `ProxyLibrary.h` header file and call `ProxyLibrary_Load` in `DllMain` during `DLL_PROCESS_ATTACH`, and call `ProxyLibrary_Unload` during `DLL_PROCESS_DETACH`.

8. Compile the project to generate the proxy DLL file for hooking.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
