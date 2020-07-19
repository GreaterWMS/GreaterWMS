var get_request_data = [{
          id: 1,
          name: 'url',
          dec: '发起请求的API_URL地址',
          com: '必填项'
        }, {
          id: 2,
          name: 'method',
          dec: 'get',
          com: '必填项'
        }, {
          id: 3,
          name: 'headers',
          dec: '请求头',
          com: '必填项',
          children: [{
              id: 31,
          name: 'Content-Type',
          dec: 'application/json;charset=utf-8',
          com: '必填项'
          }]
        }, {
          id: 4,
          name: 'params',
          dec: 'url传参',
          com: '必填项',
    hasChildren:true
        },{
          id: 5,
          name: 'data',
          dec: 'get请求不需要传data数据',
          com: '不填'
        }]
var load1getparams = [{
              id: 41,
          name: 'token',
          dec: '你的openid',
          com: '必填项'
          },{
              id: 42,
          name: 'page',
          dec: '请求哪一页的数据，默认为第一页',
          com: '可选'},{
              id: 43,
          name: 'max_page',
          dec: '每页最大数据条数，默认为100条每页，最大1000条每页',
          com: '可选'},{
              id: 44,
          name: 'sort',
          dec: '数据的排序方式，倒序请在字段名前加"-"，默认为"-create_time"',
          com: '可选'},{
              id: 45,
          name: 'name',
          dec: '根据名称模糊匹配对应的数据条',
          com: '可选'},{
              id: 46,
          name: 'status',
          dec: '根据status匹配对应的数据条',
          com: '可选'},{
              id: 47,
          name: 'transaction_code',
          dec: '根据后台唯一码匹配对应的数据条',
          com: '可选'},{
              id: 48,
          name: 'start_date_create',
          dec: '按创建时间筛选，开始的日期，格式:"2019-01-01"，与end_date同时传入后台',
          com: '可选'},{
              id: 49,
          name: 'end_date_create',
          dec: '按创建时间筛选，结束的日期，格式:"2020-01-01"，与start_date同时传入后台，默认为今天',
          com: '可选'},{
              id: 410,
          name: 'start_date_update',
          dec: '按更新时间筛选，开始的日期，格式:"2019-01-01"，与end_date同时传入后台',
          com: '可选'},{
              id: 411,
          name: 'end_date_update',
          dec: '按更新时间筛选，结束的日期，格式:"2020-01-01"，与start_date同时传入后台，默认为今天',
          com: '可选'}]

var get_back_data = [{
          id: 1,
          name: 'count',
          dec: '总共有多少条数据'
        }, {
          id: 2,
          name: 'next',
          dec: '是否有下一页，如果没有下一页，显示为null；有下一页，就显示url链接'
        }, {
          id: 3,
          name: 'previous',
          dec: '是否有上一页，如果没有上一页，显示为null；有上一页，就显示url链接'
        }, {
          id: 4,
          name: 'results',
          dec: '返回的服务器反馈结果',
    children: [{
              id: 41,
          name: 'code',
          dec: '服务器返回的数据code'
          },{
              id: 42,
          name: 'msg',
          dec: '服务器返回的数据code描述'
    },{
              id: 43,
          name: 'data',
          dec: '服务器返回的数据明细',
        hasChildren: true
          }]
}]

var load1getlist = [{
              id: 431,
          name: 'name',
          dec: '名称'
        },{
              id: 432,
          name: 'status',
          dec: '状态，一般为启用和禁用'
        },{
              id: 435,
          name: 'transaction_code',
          dec: '该条数据的服务器唯一码，此码可以在对数据进行处理的时候使用'
        },{
              id: 436,
          name: 'create_time',
          dec: '该条数据的创建时间'
        },{
              id: 435,
          name: 'last_update_time',
          dec: '该条数据的最后更新时间'
        }]

var post_request_data = [{
          id: 1,
          name: 'url',
          dec: '发起请求的API_URL地址',
          com: '必填项'
        }, {
          id: 2,
          name: 'method',
          dec: 'post',
          com: '必填项'
        }, {
          id: 3,
          name: 'headers',
          dec: '请求头',
          com: '必填项',
          children: [{
              id: 31,
          name: 'Content-Type',
          dec: 'application/json;charset=utf-8',
          com: '必填项'
          }]
        }, {
          id: 4,
          name: 'params',
          dec: 'url传参',
          com: '必填项',
            children: [{
              id: 41,
          name: 'token',
          dec: '你的openid',
          com: '必填项'
          }]
},{
          id: 5,
          name: 'data',
          dec: 'data是传一组json数组对象,支持批量创建,批量创建仅支持100条每次，例：[{"example":"1"},{"example":"2"}]',
          com: '必填项',
            hasChildren: true
        }]

var load1post = [{
              id: 431,
          name: 'name',
          dec: '名称，空值和重复数据不会被存储',
        com: '必填项'
        },{
              id: 432,
          name: 'status',
          dec: '状态，一般为启用和禁用，默认为空',
    com: '可选',
        }]

var post_back_data = [{
          id: 1,
          name: 'code',
          dec: '服务器返回的数据code'
        }, {
          id: 2,
          name: 'msg',
          dec: '服务器返回的数据code描述'
        }, {
          id: 3,
          name: 'data',
          dec: '请求的数据明细',
          hasChildren:true
        }]

var load1postdata = [{
              id: 31,
          name: 'name',
          dec: '服务器存储的名称',
        com: '必填项'
        },{
              id: 32,
          name: 'status',
          dec: '服务器存储的状态',
    com: '可选',
        }]

var patch_request_data = [{
          id: 1,
          name: 'url',
          dec: '发起请求的API_URL地址',
          com: '必填项'
        }, {
          id: 2,
          name: 'method',
          dec: 'patch',
          com: '必填项'
        }, {
          id: 3,
          name: 'headers',
          dec: '请求头',
          com: '必填项',
          children: [{
              id: 31,
          name: 'Content-Type',
          dec: 'application/json;charset=utf-8',
          com: '必填项'
          }]
        }, {
          id: 4,
          name: 'params',
          dec: 'url传参',
          com: '必填项',
            children: [{
              id: 41,
          name: 'token',
          dec: '你的openid',
          com: '必填项'
          }]
},{
          id: 5,
          name: 'data',
          dec: 'data是传一组json数组对象,支持批量创建,批量创建仅支持100条每次，例：[{"example":"1"},{"example":"2"}]',
          com: '必填项',
            hasChildren: true
        }]

var load1patch = [{
              id: 431,
          name: 'transaction_code',
          dec: '该条数据唯一码，用来匹配后台唯一的一条数据',
        com: '必填项',
        },{
              id: 432,
          name: 'name',
          dec: '名称，空值和重复数据不会被存储',
        com: '可选'
        },{
              id: 433,
          name: 'status',
          dec: '状态，一般为启用和禁用，默认为空',
    com: '可选',
        }]

var delete_request_data = [{
          id: 1,
          name: 'url',
          dec: '发起请求的API_URL地址',
          com: '必填项'
        }, {
          id: 2,
          name: 'method',
          dec: 'delete',
          com: '必填项'
        }, {
          id: 3,
          name: 'headers',
          dec: '请求头',
          com: '必填项',
          children: [{
              id: 31,
          name: 'Content-Type',
          dec: 'application/json;charset=utf-8',
          com: '必填项'
          }]
        }, {
          id: 4,
          name: 'params',
          dec: 'url传参',
          com: '必填项',
            children: [{
              id: 41,
          name: 'token',
          dec: '你的openid',
          com: '必填项'
          }]
},{
          id: 5,
          name: 'data',
          dec: 'data是传一组json数组对象,支持批量创建,批量创建仅支持100条每次，例：[{"example":"1"},{"example":"2"}]',
          com: '必填项',
            hasChildren: true
        }]

var load1delete = [{
              id: 431,
          name: 'transaction_code',
          dec: '该条数据唯一码，用来匹配后台唯一的一条数据',
        com: '必填项',
        }]