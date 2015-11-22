local key = "--(i_love_niu)--"
local iv = "--(i_love_niu)--"
local plain = "iloveniu"
local AES = require "pycrypto_aes"

--现在情况只能加密16* 的字符串，为了能加密任意长度字符，需要一个pad
--加密前加入pad 解密后除去pad pad的选择根据实际情况 { 还算凑合

local addpad = function(plain, pad, size)
    local bsize = size or 16
    local pad = pad or "{"
    local n = bsize - string.len(plain)%bsize
    return plain..string.rep(pad, n)
end

local cleanpad = function(plain, pad)
    local pad = pad or "{"
    local res, _  = string.gsub(plain, pad.."*$", '')
    return res
end

local testfunc = function(key, mode, iv) 
	local aes = AES.new(key, mode, iv)
	local cipher = ngx.encode_base64(aes:encrypt(addpad(plain)))
	ngx.say(cipher)

	local enc = ngx.decode_base64(cipher)
	aes = AES.new(key, mode, iv)
	ngx.say(cleanpad(aes:decrypt(enc )))
end

testfunc(key, AES.MODE_CBC, iv)
--testfunc(key, AES.MODE_CFB, iv)
--testfunc(key, AES.MODE_OFB, iv)

--curl 'http://127.0.0.1:8000/api/aespy'
--pycrypot_aes from https://github.com/orangle/lua-pycrypto-aes
