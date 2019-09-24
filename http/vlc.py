import vlc
i = vlc.Instance('--verbose 2'.split())
p = i.media_player_new()
p.set_mrl('rtmp://videofms.100xuexi.com/xxv/mp4:streams/kaoyangonggongkezhengzhi/kaoyangonggongkezhengzhizhentijiexiban/9012nian/VideoC/90180210_092501/d6c57c74-f440-be61-5796-92c4d33.mp4')
p.play()