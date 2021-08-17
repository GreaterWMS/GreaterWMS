# Docker

## 命令

### 构建

```sh
docker build --tag wms:$VERSION .
```

### 运行

```sh
docker run --publish 80:80 --name wms wms:$VERSION
```
