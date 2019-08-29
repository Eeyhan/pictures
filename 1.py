    def request_url(self, url, url_name, proxy=None, args_urlencode=None, args=None):
        """
        请求单个网址
        :param url: url
        :param url_name: url别名
        :param proxy: 代理
        :param args_urlencode: 已编码的搜索职位名参数
        :param args: 未编码的搜索职位名参数
        :return:
        """
        # 索引字段
        index = args

        # 中华英才网相关
        chinahr_url = 'http://www.chinahr.com/jobs/'

        if not args_urlencode:
            args_urlencode = urllib.parse.quote('python')
        # for i in range(1, 4):
        for i in range(1, 2):
            # 卓聘相关
            zhuopin_data = {
                'CID': '',
                'Q': args_urlencode,
                'pageIndex': i,
                'pageSize': '20',
                'ReferrerType': '',
                'qTitle': '1',
                'JobLocation': '',
                'CompanyIndustry': '',
                'JobType': '',
                'AnnualSalaryMin': '-1',
                'AnnualSalaryMax': '-1',
                'CompanyType': '',
                'ReleaseDate': '',
                'GID': '1e597c4a-7bae-483e-9807-41a583778abc'
            }

            # 拉钩相关
            lagou_data = {
                'first': 'false',
                'pn': i,
                'kd': args_urlencode,
            }

            lagou_start_url = 'https://www.lagou.com/jobs/list_{args}?px=default&city=%E5%85%A8%E5%9B%BD'.format(
                args=args_urlencode)

            # 大街网相关
            dajie_start_url = 'https://so.dajie.com/job/search?keyword={args}'.format(args=args_urlencode)

            # 中国人才热线相关
            cjol_data = {
                'KeywordType': '3',
                'KeyWord': args_urlencode,
                'SearchType': '3',
                'ListType': '2',
                'page': i
            }

            # 卓聘人才网
            jobcn_data = {
                'p.querySwitch': '0',
                'p.searchSource': 'default',
                'p.keyword': args_urlencode,
                'p.keyword2': '',
                'p.keywordType': '0',
                'p.pageNo': i,
                'p.pageSize': '40',
                'p.sortBy': 'postdate',
                'p.statistics': 'false',
                'p.totalRow': '72',
                'p.cachePageNo': i,
                'p.cachePosIds': '3996831,3867032,3854083,4025644,200431,4049685,4093100,4049690,3410415,3955832,4073900,4041020,3574331,3574330,4021063,3319026,4022062,4076046,4076044,4065380,4067051,3939390,4082129,3920851,4025383,4046472,4089204,4064692,4061820,4093697,3852019,4087419,4087053,2269732,3933028,4071237,4042056,4063573,4037702,3663255,3145932,3915673,3908465,3776789,4025742,4071540,3095066,4052562,4052555,4052546,4052543,4025179,3741319,3812596,4045056,4033451,4033373,3615871,3782627,4022040,4005016,3727904,3996067,3903386,3903347,2977257,3697238,3992534,3908819,3865892,3795130,3737555',
                'p.cachePosUpddates': '201908111448,201908111448,201908111422,201908111330,201908111319,201908111000,201908110823,201908110711,201908101150,201908101143,201908091725,201908091506,201908091133,201908091133,201908091100,201908091057,201908091020,201908090839,201908090839,201908090839,201908080951,201908080850,201908080823,201908071523,201908070846,201908061025,201908061000,201908050854,201908031518,201908031339,201908011610,201907301006,201907221455,201907171044,201907161443,201907110813,201907071014,201907011744,201906300818,201906211309,201906181016,201906091016,201906091016,201906030906,201905290840,201905240300,201904271038,201904020300,201904020300,201904020300,201904020300,201903290918,201903281543,201903271520,201903150300,201902190300,201902190300,201902101649,201901190854,201901021430,201901010910,201811211054,201811141644,201810311054,201810311054,201810170953,201810150929,201810101042,201810101042,201809130935,201809130935,201808271719',
                'p.jobnature': '15',
                'p.comProperity': '0',
                'p.JobLocationTown': '',
                'p.salary': '-1',
                'p.highSalary': '100000',
                'p.salarySearchType': '1',
                'p.includeNeg': '1',
                'p.inputSalary': '-1',
                'p.workYear1': '-1',
                'p.workYear2': '11',
                'p.degreeId1': '10',
                'p.degreeId2': '70',
                'p.posPostDate': '366',
                'p.otherFlag': '3',
            }

            if 'zhilian' in url_name:
                # city_code = self.get_zhilian_city_code()
                i *= 90
                url = url.format(c='{c}', p=i, q=args_urlencode)
            elif 'parser_ganji' == url_name:
                # city_code = self.ganji_city_codes()
                url = url.format(c='{c}', p=i, q=args)
            elif 'parser_ganji_it' == url_name:
                # city_code = self.ganji_city_codes()
                # city_code = 'bj'
                i = (i - 1) * 32
                url = url.format(c='{c}', p=i, q=args_urlencode)
            elif '58' in url_name:
                # city_code = self.get_58_city_code()
                # city_code = 'bj'
                url = url.format(c='{c}', p=i, q=args_urlencode)
            elif 'parser_chinahr' == url_name:
                # city_code = self.get_chinahr_city_code()
                # city_code = 'bj'
                url = url.format(c='{c}', p=i, q=args_urlencode)
            elif 'gongzuochong' in url_name:
                # city_code = self.get_gzc_city_code()
                # city_code = 'bj'
                url = url.format(c='{c}', p=i, q=args_urlencode)
            elif 'baidu' in url_name:
                city_code = self.get_baidu_city_code()
                # city_code = '上海'
                city_code1 = urllib.parse.quote(city_code)
                city_code2 = urllib.parse.quote(city_code1)

                # 百度百聘的api把城市参数做了两层url编码
                token_url = 'https://zhaopin.baidu.com/quanzhi?city={c}&query={q}'.format(c=city_code1,
                                                                                          q=args_urlencode)
                token = self.get_baidu_token(token_url, url_name)
                if i == 1:
                    i -= 1
                i *= 20
                url = url.format(c=city_code2, p=i, q=args_urlencode, token=token)

            elif 'liepin' in url_name:
                i -= 1
                url = url.format(p=i, q=args_urlencode)
            elif 'yjs' in url_name:
                i -= 1
                if i < 0:
                    i = 0
                i *= 10
                url = url.format(p=i, q=args_urlencode)
            elif 'jobcn' in url_name:
                pass
            elif url_name == 'jiaoshizhaopin':
                args = urllib.parse.quote(args, encoding='gb2312')
                url = url.format(p=i, q=args)
            elif 'shuobo' in url_name and i == 1:
                url = 'http://www.51shuobo.com/s/result/kt1_kw-{q}/'.format(q=args_urlencode)

            elif 'job1001' in url_name:
                i -= 1
                url = url.format(p=i, q=args_urlencode)
            elif 'linkin' in url_name:
                city = '中国'
                c = urllib.parse.quote(city)
                if i == 1:
                    i = 0
                i *= 25
                url = url.format(c=c, p=i, q=args_urlencode)

            elif 'telecomhr' in url_name:
                args = urllib.parse.quote(args, encoding='gb2312')
                url = url.format(p=i, q=args)

            else:
                url = url.format(p=i, q=args_urlencode)

            # 开始请求
            try:
                if 'zhilian' in url_name:
                    city_codes = self.get_zhilian_city_code()
                    for c in city_codes:
                        url = url.format(c=c)
                        response = requests.get(url, headers=self.header, proxies=proxy, timeout=(3, 7), verify=False)

                elif 'zhuopin' in url_name:
                    response = requests.post(url, headers=self.header, data=zhuopin_data, proxies=proxy, timeout=(3, 7),
                                             verify=False)
                elif 'lagou' in url_name:
                    cookie = self.get_cookie(lagou_start_url)
                    response = requests.post(url, headers=self.header, data=lagou_data, proxies=proxy, timeout=(3, 7),
                                             verify=False, cookies=cookie)
                elif 'dajie' in url_name:

                    # 神奇，大街网不能更新header，只能直接设置header,应该有字段顺序关系
                    header = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'User-Agent': random.choice(USER_AGENT),
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Connection': 'keep-alive',
                        'Accept-Encoding': 'gzip, deflate',
                        'Upgrade-Insecure-Requests': '1',
                        'dnt': '1',
                        'x-requested-with': 'XMLHttpRequest',
                        'referer': 'https://so.dajie.com/job/search?keyword={q}&from=job&clicktype=blank'.format(
                            q=args_urlencode)
                    }

                    cookie = self.get_cookie(dajie_start_url, url_name, args_urlencode)
                    response = requests.get(url, headers=header, proxies=proxy, timeout=(3, 7), verify=False,
                                            cookies=cookie)
                elif 'chinahr_old' in url_name:
                    cookie = self.get_cookie(chinahr_url, url_name, args_urlencode)
                    response = requests.get(url, header=self.header, proxies=proxy, timeout=(3, 7), verify=False,
                                            cookies=cookie)

                elif 'cjol' in url_name:
                    header = self.header
                    header.update({
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'dnt': '1',
                        'x-requested-with': 'XMLHttpRequest',
                    })
                    response = requests.post(url, headers=header, proxies=proxy, timeout=(3, 7), verify=False,
                                             data=cjol_data)
                elif 'jobcn' in url_name:
                    response = requests.post(url, headers=self.header, proxies=proxy, timeout=(3, 7), verify=False,
                                             data=jobcn_data)
                elif 'doumi' in url_name:
                    city_code = self.get_doumi_city_codes()
                    # city_code = 'bj'
                    doumi_url = self.DOUMI_COOKIE_URL % city_code
                    session = self.get_session(url_name, doumi_url)
                    response = session.get(url, headers=self.header, proxies=proxy, timeout=(3, 7), verify=False)

                elif 'boss' in url_name:
                    header = self.header
                    header.update(BOSS_COOKIE)
                    response = requests.get(url, headers=header, proxies=proxy, timeout=(3, 7), verify=False)

                else:
                    response = requests.get(url, headers=self.header, proxies=proxy, timeout=(3, 7), verify=False)
                if response.status_code == 200:
                    # 解析网站
                    html = self.decode_request(response)
                    result = self.parser(html, url_name, url, args_urlencode, index=index)
                    return result
                else:
                    pass

            except Exception as e:
                if self.proxy_list:
                    self.proxy_list.remove(proxy)
                    proxy = self.get_proxy()
                if 'zhuopin' in url_name:
                    response = requests.post(url, headers=self.header, data=zhuopin_data, proxies=proxy, timeout=(3, 7),
                                             verify=False)
                elif 'dajie' in url_name:
                    print(e)
                elif 'lagou' in url_name:
                    pass
                    # cookie = self.get_lagou_cookie(lagou_start_url)
                    # response = requests.post(url, headers=self.header, data=lagou_data, proxies=proxy, timeout=(3, 7),
                    #                          verify=False, cookies=cookie)
                else:
                    response = requests.get(url, headers=self.header, proxies=proxy, timeout=(3, 7), verify=False)
                html = self.decode_request(response)
                self.parser(html, url_name, url, args_urlencode, index=index)