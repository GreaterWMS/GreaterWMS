<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <p>完全开源的仓库管理系统</p>
</div>

写这套软件的愿景是让他成为一个框架，方便所有人进行仓库管理的软件开发，而后来发现，我们把他写成一套软件了，这不是我们愿意看到的

所以，我们用Rust重构了底层，用python作为载体，写了一套新的CLI底层框架[Bomiot](https://gitee.com/Bomiot/Bomiot),高性能，更方便便捷的开发，完全发挥python本身的语言优势

旧版GreaterWMS文件地址，可以在这里找到：
[GreaterWMS v2.1.49](https://gitee.com/Singosgu/GreaterWMS/tree/V2.1.49)

GreaterWMS 也将使用[Bomiot](https://gitee.com/Bomiot/Bomiot)，进行3.0重构