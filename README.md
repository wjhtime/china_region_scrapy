# 中国地区爬虫scrapy版

使用scrapy框架爬中国省市地区数据，5级页面

之前写过 [多进程版本](https://github.com/wjhtime/china_region_spider)，本以为多进程速度很快了，但是跟scrapy比起来还是有差别，scrapy爬取全部页面70+万数据只用20多分钟，速度相当快！

数据整理之后放到了[地区数据库](https://github.com/wjhtime/china_regions) 这个项目里面，可以直接拿来使用


## Quick Start

```
1. 执行建表语句
2. cd region
3. scrapy crawl region
```


## Feature

- 数据更新，取的2017年的城市数据(2018年的还未出)
- 多级采集，共5级页面
- 日志记录文件，只记录info类型的信息
- 全部爬完只需20多分钟，共计70+万数据


## 表结构

| 字段     | 备注             |
| ------ | -------------- |
| id     | 主键             |
| p_code | 上一级编码          |
| code   | 编码             |
| name   | 名称             |
| url    | 当前的城市链接，供下一次采集 |
| level  | 级别             |


### 建表语句

```mysql
CREATE TABLE `china_regions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `p_code` varchar(50) NOT NULL DEFAULT '' COMMENT '上一级编码',
  `code` varchar(50) NOT NULL DEFAULT '' COMMENT '编码',
  `name` varchar(100) NOT NULL DEFAULT '' COMMENT '名称',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '链接',
  `level` tinyint(4) NOT NULL COMMENT '级别:1-省，2-市，3-县，4-镇，5-村委会',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```



## To Do List

- 性能优化
- 错误处理
- 去重操作


## 遇到的坑

- 部分页面只有tr标签，没有a标签，此处需进行错误处理，判断是否可以解析到数据
- 由于对yield了解不够深入，导致数据总是缺失，所以必须在每个parse方法中需要使用两个yield语句

## CHANGELOG

[CHANGELOG](https://github.com/wjhtime/china_region_scrapy/releases)


## License

[MIT](https://github.com/wjhtime/china_region_scrapy/blob/master/LICENSE)
