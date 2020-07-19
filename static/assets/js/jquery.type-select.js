(function($){
	$.fn.typeSelect = function(method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(
                    arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Method ' + method + ' does not exist on jQuery.typeSelect');
        }
    };
    $.fn.typeSelect._default = {
        data : null,
        value : null,
        scope : null,
        field : 'id',
        pField : 'pId',
        nameField : 'name',
        style : null,
        class : null,
        callback : null
	};
    var methods = {
    	_optionsDetail : null,
        init : function(_options){
           new TypeSelectClass(_options,$(this));
        }
    };
    var TypeSelectClass = function(){
    	this.init.apply(this, arguments);
    };
    TypeSelectClass.prototype = {
		_options : null,
    	_targetDom : null,
    	init : function(_options,container){
    	   this._options = $.extend({},$.fn.typeSelect._default,_options);
    	   this._targetDom = container;
    	   this._targetDom.empty();
    	   if(_options.value && _options.value != "undefined"){
    	   	   this._initTypeSelectWithValue(_options.value,1);
    	   	   if(_options.scope){
    				var html = '<input id="'+_options.scope+'" name="'+_options.scope+'" value="'+_options.value+'" type="hidden"/>';
    				this._targetDom.prepend(html);
    		   }
    	   }else{
	    	   this._initTypeSelect();
    	   }
    	},
    	_initTypeSelect : function(){
    		var _options = this._options;
    		var _data = _options.data;
    		var _randomStrId = Math.floor(Math.random()*10000000000)+"typeSelect";
    		var html = '';
    		if(_options.scope){
    			html += '<input id="'+_options.scope+'" name="'+_options.scope+'" value="" type="hidden"/>';
    		}
    		html += '<select id="'+_randomStrId+'" class="PUFilterSelect01 '+_options.class+'" style="'+_options.style+'">';
    		html += '<option value="">-请选择-</option>';
    		for(var i=0;i<_data.length;i++){
    			if(!_data[i][_options.pField]){
	    			html += '<option value="'+_data[i][_options.field]+'">'+_data[i][_options.nameField]+'</option>';
    			}
    		}
    		html += '</select>';
    		this._targetDom.append(html);
    		this._bindTypeSelectChanges(_randomStrId);
    	},
    	_initTypeSelectWithValue : function(value,index){
    		var _options = this._options;
    		var _data = _options.data;
    		var _value = value;
    		var _pCode = "";
    		var _obj = this._getObject(_value);
    		if(_obj){
    			_pCode = _obj[_options.pField];
    		}
    		if(index==1){
    			_pCode = value;
    		}
    		var optionHtml = '';
    		for(var i=0;i<_data.length;i++){
    			if(_pCode){
    				if(_data[i][_options.pField] == _pCode){
    					if(_value == _data[i][_options.field]){
    						optionHtml += '<option value="'+_data[i][_options.field]+'" selected="selected">'+_data[i][_options.nameField]+'</option>';
    					}else{
    						optionHtml += '<option value="'+_data[i][_options.field]+'">'+_data[i][_options.nameField]+'</option>';
    					}
    				}
    			}else{
    				if(!_data[i][_options.pField]){
    					if(_value == _data[i][_options.field]){
    						optionHtml += '<option value="'+_data[i][_options.field]+'" selected="selected">'+_data[i][_options.nameField]+'</option>';
    					}else{
    						optionHtml += '<option value="'+_data[i][_options.field]+'">'+_data[i][_options.nameField]+'</option>';
    					}
    				}
    			}
    		}
    		if(optionHtml) {
    			var _randomStrId = Math.floor(Math.random()*10000000000)+"typeSelect";
        		var html = '';
        		html += '<select id="'+_randomStrId+'" class="PUFilterSelect01 '+_options.class+'" style="'+_options.style+'">';
        		html += '<option value="">-请选择-</option>';
        		html += optionHtml;
        		html += '</select>';
        		this._targetDom.prepend(html);
        		this._bindTypeSelectChanges(_randomStrId);
    		}
    		if(_pCode){
    			index ++;
	    		this._initTypeSelectWithValue(_pCode,index);
    		}
    	},
    	_getObject : function(value){
    		var _options = this._options;
    		var _data = _options.data;
    		if(_data && _data.length > 0){
    			for(var i=0;i<_data.length;i++){
    				if(_data[i][_options.field] == value){
    					return _data[i];
    				}
    			}
    		}
    		return null;
    	},
    	_bindTypeSelectChanges : function(id){
    		var _options = this._options;
    		var _data = _options.data;
	    	var _changeDom = $("#"+id);
	    	var _this = this;
    		_changeDom.unbind("change").bind("change",function(){
	    		var _randomStrId = Math.floor(Math.random()*10000000000)+"typeSelect";
	    		_changeDom.nextAll().remove();
    			var _hasChild = false;
    			var html = '<select id="'+_randomStrId+'" class="PUFilterSelect01 '+_options.class+'" style="margin-left:10px;'+_options.style+'">';
    			html += '<option value="">-请选择-</option>';
    			for(var i=0;i<_data.length;i++){
    				if(_changeDom.val() && _changeDom.val() == _data[i][_options.pField]){
	    				html += '<option value="'+_data[i][_options.field]+'">'+_data[i][_options.nameField]+'</option>';
	    				_hasChild = true;
    				}
    			}
    			html += '</select>';
    			if(_hasChild){
    				_this._targetDom.append(html);
    				_this._bindTypeSelectChanges(_randomStrId);
    			}
    			var _changeDomVal = _changeDom.val();
    			var _changePDom = _changeDom.prev("select");
    			if(!_changeDomVal && _changePDom.length>0){
    				$("#"+_options.scope).val(_changePDom.val());
    			}else{
    				$("#"+_options.scope).val(_changeDomVal);
    			}
    			if(_options.callback){
    				_options.callback(_this._getObject(_changeDomVal));
    			}
    		});
    	}
	};
})(jQuery)