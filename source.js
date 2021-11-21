submitForm: function(t) {
    var e = this
      , n = this
      , s = Object.assign({}, n.ruleForm)
      , a = "user/register/email";
    if (n.resetError(),
    "info" == n.buttonType)
        return !1;
    if (1 == n.radio && delete s.phone,
    2 == n.radio) {
        var o = n.ruleForm.countryList.filter((function(t) {
            return t.areaCode == n.ruleForm.state
        }
        ));
        if (0 == o.length)
            return n.phoneError = this.$t("lang.register.errorInfo"),
            !1;
        s.countryId = o[0].id,
        delete s.state,
        delete s.email,
        a = "user/register/phone"
    }
    n.showloading = !0,
    n.$http.post(a, this.qs.stringify(s)).then((function(t) {
        if (n.showloading = !1,
        0 === t.code)
            n.utils.logEvent("userRegisterTimeEvent", {
                registerDate: new Date
            }),
            n.utils.alert(e.$t("lang.register.note"), e.$t("lang.register.registerInfo")).then((function() {
                n.$router.push("/login")
            }
            ));
        else if (-3 === t.code) {
            var s = t.msg.split(";");
            s.forEach((function(t, e, s) {
                var a = t.split(":")[0]
                  , o = t.split(":")[1];
                n[a + "Error"] = o
            }
            ))
        }
    }
    ))
},
