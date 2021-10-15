import smtplib
import email.message


class Message:
    def message_true(code, name_cert, name, price, mail):

        email_content = """
            <html>

            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
            <style type="text/css">
                table,
                td {
                    border-collapse: collapse;
                }

                img {
                    border: 0;
                    height: auto;
                    line-height: 100%;
                    outline: none;
                    text-decoration: none;
                }

                a {
                    text-decoration: none;
                }

                p {
                    font-size: 14px;
                    line-height: 1.5;
                    margin: 0 0 10px 0;
                }

                ul {
                    margin: 0 0 10px 0;
                }

                ul>li {
                    font-size: 14px;
                    line-height: 1.5;
                    margin: 0;
                }

                h1,
                h2,
                h3,
                h4,
                h5,
                h5 {
                    line-height: 1.2;
                    margin: 0 0 10px 0;
                    font-weight: normal;
                }

                h1 {
                    font-size: 36px;
                }

                h2 {
                    font-size: 30px;
                }

                h3 {
                    font-size: 24px;
                }

                h4 {
                    font-size: 20px;
                }

                h5 {
                    font-size: 14px;
                }

                hr {
                    margin: 0;
                }

                th.tc,
                th.social_element {
                    font-weight: normal;
                    text-align: left;
                }

                tr,
                td,
                th {
                    border-color: transparent;
                }

                .content-cell {
                    vertical-align: top;
                }

                .content-cell table.sp-button,
                .content-cell table.social,
                .content-cell table.sp-button td,
                .content-cell table.social td,
                .content-cell table.sp-button th,
                .content-cell table.social th,
                .content-cell table.sp-button table,
                .content-cell table.social table {
                    border-color: transparent;
                    border-width: 0;
                    border-style: none;
                    border: 0;
                }

                .content-cell table.sp-button td,
                .content-cell table.social td,
                .content-cell table.sp-button th,
                .content-cell table.social th {
                    padding: 0;
                }

                .content-cell table.social {
                    line-height: 1;
                }

                .content-cell>center>.sp-button {
                    margin-left: auto;
                    margin-right: auto;
                }

                .content-cell .sp-button table td {
                    line-height: 1;
                }

                .content-cell .sp-button-side-padding,
                .content-cell .sp-button-text,
                .content-cell .social,
                .content-cell .social_element {
                    border-color: transparent;
                    border-width: 0;
                    border-style: none;
                }

                .content-cell .sp-button-side-padding {
                    width: 21px;
                }

                .content-cell .sp-button-text a {
                    text-decoration: none;
                    display: block;
                }

                .content-cell .sp-button-text a img {
                    max-width: 100%;
                }

                .content-cell span[style*="color"]>a {
                    color: inherit;
                }

                .content-cell>div>.sp-img,
                .content-cell>div>a>.sp-img {
                    margin: 0;
                }

                .content-cell .link_img {
                    display: block;
                }

                .content-cell .sp-button-img td {
                    display: table-cell !important;
                    width: initial !important;
                }

                .email-text>p,
                .content-cell>p {
                    line-height: inherit;
                    color: inherit;
                    font-size: inherit;
                }

                .email-text em,
                .content-cell em {
                    color: inherit;
                }

                .email-text>table,
                .content-cell>table {
                    border-color: #ddd;
                    border-width: 1px;
                    border-style: solid;
                }

                .email-text>table>tr>td,
                .content-cell>table>tr>td,
                .email-text>table>tr>th,
                .content-cell>table>tr>th,
                .email-text>table>tbody>tr>td,
                .content-cell>table>tbody>tr>td,
                .email-text>table>tbody>tr>th,
                .content-cell>table>tbody>tr>th {
                    border-color: #ddd;
                    border-width: 1px;
                    border-style: solid;
                }

                .email-text>table td,
                .content-cell>table td,
                .email-text>table th,
                .content-cell>table th {
                    padding: 3px;
                }

                .social_element,
                .content-cell table.social .social_element {
                    padding: 2px 5px;
                    font-size: 13px;
                    font-family: Arial, sans-serif;
                    line-height: 32px;
                }

                .social_element img.social,
                .content-cell table.social .social_element img.social {
                    display: block;
                }

                .content-cell table.social .social_element_t_3 img.social,
                .content-cell table.social .social_element_t_4 img.social,
                .content-cell table.social .social_element_t_5 img.social,
                .content-cell table.social .social_element_v_i_t img.social {
                    display: inline;
                }

                .email-text pre {
                    background-color: transparent;
                    border: 0;
                    color: inherit;
                    padding: 0;
                    margin: 1em 0;
                }

                .email-wrapper span[style*="color"]>a {
                    color: inherit;
                }

                .sp-video a {
                    display: block;
                    overflow: auto;
                }

                .sp-video img {
                    max-width: 100%;
                }

                @media only screen and (max-width: 640px) {
                    .sp-hidden-mob {
                        display: none !important;
                    }
                }

                a {
                    color: #000000;
                }

                body,
                .content-row,
                p,
                h1,
                h2,
                h3,
                h4,
                h5,
                h6,
                li {
                    color: #444444;
                    font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;
                }

                body,
                table,
                div,
                p,
                li {
                    font-size: 14px;
                    line-height: 1.2;
                }
            </style>
            <style type="text/css">
                /* SendPulse custom CSS Reset */
                table,
                td {
                    border-collapse: collapse;
                }

                img {
                    border: 0;
                    height: auto;
                    line-height: 100%;
                    outline: none;
                    text-decoration: none;
                }

                a {
                    text-decoration: none;
                }

                p {
                    font-size: 14px;
                    line-height: 1.5;
                    margin: 0 0 10px 0;
                }

                ul {
                    margin: 0 0 10px 0;
                }

                ul>li {
                    font-size: 14px;
                    line-height: 1.5;
                    margin: 0;
                }

                h1,
                h2,
                h3,
                h4,
                h5,
                h5 {
                    line-height: 1.2;
                    margin: 0 0 10px 0;
                    font-weight: normal;
                }

                h1 {
                    font-size: 36px;
                }

                h2 {
                    font-size: 30px;
                }

                h3 {
                    font-size: 24px;
                }

                h4 {
                    font-size: 20px;
                }

                h5 {
                    font-size: 14px;
                }

                hr {
                    margin: 0;
                }

                th.tc,
                th.social_element {
                    font-weight: normal;
                    text-align: left;
                }

                tr,
                td,
                th {
                    border-color: transparent;
                }

                .content-cell {
                    vertical-align: top;
                }

                .content-cell table.sp-button,
                .content-cell table.social,
                .content-cell table.sp-button td,
                .content-cell table.social td,
                .content-cell table.sp-button th,
                .content-cell table.social th,
                .content-cell table.sp-button table,
                .content-cell table.social table {
                    border-color: transparent;
                    border-width: 0;
                    border-style: none;
                    border: 0;
                }

                .content-cell table.sp-button td,
                .content-cell table.social td,
                .content-cell table.sp-button th,
                .content-cell table.social th {
                    padding: 0;
                }

                .content-cell table.social {
                    line-height: 1;
                }

                .content-cell>center>.sp-button {
                    margin-left: auto;
                    margin-right: auto;
                }

                .content-cell .sp-button table td {
                    line-height: 1;
                }

                .content-cell .sp-button-side-padding,
                .content-cell .sp-button-text,
                .content-cell .social,
                .content-cell .social_element {
                    border-color: transparent;
                    border-width: 0;
                    border-style: none;
                }

                .content-cell .sp-button-side-padding {
                    width: 21px;
                }

                .content-cell .sp-button-text a {
                    text-decoration: none;
                    display: block;
                }

                .content-cell .sp-button-text a img {
                    max-width: 100%;
                }

                .content-cell span[style*="color"]>a {
                    color: inherit;
                }

                .content-cell>div>.sp-img,
                .content-cell>div>a>.sp-img {
                    margin: 0;
                }

                .content-cell .link_img {
                    display: block;
                }

                .content-cell .sp-button-img td {
                    display: table-cell !important;
                    width: initial !important;
                }

                .email-text>p,
                .content-cell>p {
                    line-height: inherit;
                    color: inherit;
                    font-size: inherit;
                }

                .email-text em,
                .content-cell em {
                    color: inherit;
                }

                .email-text>table,
                .content-cell>table {
                    border-color: #ddd;
                    border-width: 1px;
                    border-style: solid;
                }

                .email-text>table>tr>td,
                .content-cell>table>tr>td,
                .email-text>table>tr>th,
                .content-cell>table>tr>th,
                .email-text>table>tbody>tr>td,
                .content-cell>table>tbody>tr>td,
                .email-text>table>tbody>tr>th,
                .content-cell>table>tbody>tr>th {
                    border-color: #ddd;
                    border-width: 1px;
                    border-style: solid;
                }

                .email-text>table td,
                .content-cell>table td,
                .email-text>table th,
                .content-cell>table th {
                    padding: 3px;
                }

                .social_element,
                .content-cell table.social .social_element {
                    padding: 2px 5px;
                    font-size: 13px;
                    font-family: Arial, sans-serif;
                    line-height: 32px;
                }

                .social_element img.social,
                .content-cell table.social .social_element img.social {
                    display: block;
                }

                .content-cell table.social .social_element_t_3 img.social,
                .content-cell table.social .social_element_t_4 img.social,
                .content-cell table.social .social_element_t_5 img.social,
                .content-cell table.social .social_element_v_i_t img.social {
                    display: inline;
                }

                .email-text pre {
                    background-color: transparent;
                    border: 0;
                    color: inherit;
                    padding: 0;
                    margin: 1em 0;
                }

                .email-wrapper span[style*="color"]>a {
                    color: inherit;
                }

                .sp-video a {
                    display: block;
                    overflow: auto;
                }

                .sp-video img {
                    max-width: 100%;
                }

                @media only screen and (max-width: 640px) {
                    .sp-hidden-mob {
                        display: none !important;
                    }
                }

                /*
            CSS Helpers and Hacks
            */
                /* What it does: Remove spaces around the email design added by some email clients. */
                body {
                    margin: 0;
                    padding: 0;
                }

                /* What it does: Stops email clients resizing small text. */
                * {
                    -webkit-text-size-adjust: 100%;
                    -ms-text-size-adjust: 100%;
                }

                /* What it does: Stops Outlook from adding extra spacing to tables. */
                table,
                td {
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                /* Outlook.com hacks */
                #outlook a {
                    padding: 0;
                }

                .ReadMsgBody {
                    width: 100%;
                }

                .ExternalClass {
                    width: 100%;
                }

                .ExternalClass * {
                    line-height: 100%;
                }

                /* What it does: Uses a better rendering method when resizing images in IE. */
                img {
                    -ms-interpolation-mode: bicubic;
                }

                table {
                    margin-bottom: 0 !important;
                    border-color: transparent;
                }

                /* TARGETING Gmail */
                u~div .gmail-hide {
                    display: none;
                }

                u~div .gmail-show {
                    display: block !important;
                }

                /* TARGETING YAHOO! MAIL AND AOL */
                @media yahoo {
                    .yahoo-hide {
                        display: none;
                    }

                    .yahoo-show {
                        display: block !important;
                    }
                }

                /* What it does: Prevents Gmail from changing the text color in conversation threads. */
                .im {
                    color: inherit !important;
                }

                /*
            Ukr.net hacks
            */
                td[class^='xfmc'] {
                    width: inherit !important;
                }

                @media only screen and (max-width: 640px) {
                    .wrapper-table {
                        min-width: 296px;
                    }

                    .sp-demo-label-link {
                        display: block;
                    }

                    table {
                        width: 100% !important;
                    }

                    table,
                    hr {
                        width: 100%;
                        max-width: 100% !important;
                    }

                    td,
                    div {
                        width: 100% !important;
                        height: auto !important;
                        -webkit-box-sizing: border-box;
                        box-sizing: border-box;
                    }

                    img:not(.p100_img),
                    .content-cell img {
                        width: auto;
                        height: auto;
                        max-width: 100% !important;
                    }

                    td,
                    th {
                        display: block !important;
                        margin-bottom: 0;
                        height: inherit !important;
                    }

                    td.content-cell,
                    th.content-cell {
                        padding: 15px !important;
                    }

                    td.content-cell .social,
                    th.content-cell .social {
                        width: auto !important;
                    }

                    td.content-cell .social td .share td,
                    th.content-cell .social td .share td,
                    td.content-cell .social th,
                    th.content-cell .social th,
                    td.content-cell .share th,
                    th.content-cell .share th {
                        display: inline !important;
                        display: inline-block !important;
                    }

                    td.content-cell .social td .share td.social_element_t_3,
                    th.content-cell .social td .share td.social_element_t_3,
                    td.content-cell .social th.social_element_t_3,
                    th.content-cell .social th.social_element_t_3,
                    td.content-cell .share th.social_element_t_3,
                    th.content-cell .share th.social_element_t_3,
                    td.content-cell .social td .share td.social_element_t_4,
                    th.content-cell .social td .share td.social_element_t_4,
                    td.content-cell .social th.social_element_t_4,
                    th.content-cell .social th.social_element_t_4,
                    td.content-cell .share th.social_element_t_4,
                    th.content-cell .share th.social_element_t_4 {
                        display: block !important;
                    }

                    td.content-cell .social td .share td a>img,
                    th.content-cell .social td .share td a>img,
                    td.content-cell .social th a>img,
                    th.content-cell .social th a>img,
                    td.content-cell .share th a>img,
                    th.content-cell .share th a>img {
                        width: 32px !important;
                        height: 32px !important;
                    }

                    td.content-cell>td,
                    th.content-cell>td {
                        width: 100%;
                    }

                    td.content-cell>p,
                    th.content-cell>p {
                        width: 100% !important;
                    }

                    td.content-cell.padding-lr-0,
                    th.content-cell.padding-lr-0 {
                        padding-left: 0 !important;
                        padding-right: 0 !important;
                    }

                    td.content-cell.padding-top-0,
                    th.content-cell.padding-top-0 {
                        padding-top: 0 !important;
                    }

                    td.content-cell.padding-bottom-0,
                    th.content-cell.padding-bottom-0 {
                        padding-bottom: 0 !important;
                    }

                    .sp-video {
                        padding-left: 15px !important;
                        padding-right: 15px !important;
                    }

                    .wrapper-table>tbody>tr>td {
                        padding: 0;
                    }

                    .block-divider {
                        padding: 2px 15px !important;
                    }

                    .social_share {
                        width: 16px !important;
                        height: 16px !important;
                    }

                    .sp-button td {
                        display: table-cell !important;
                        width: initial !important;
                    }

                    .sp-button td.sp-button-side-padding {
                        width: 21px !important;
                    }

                    input {
                        max-width: 100% !important;
                    }

                    table {
                        border-width: 1px;
                    }

                    .tc {
                        width: 100% !important;
                    }

                    .small_img,
                    table.email-checkout.email-checkout-yandex {
                        width: auto !important;
                    }

                    table.smallImg td.smallImg {
                        display: inline !important;
                    }

                    .inline-item {
                        display: inline !important;
                    }

                    table.origin-table {
                        width: 95% !important;
                    }

                    table.origin-table td {
                        display: table-cell !important;
                        padding: 0 !important;
                    }

                    table.origin-table td img.small_img {
                        max-width: 120px !important;
                    }

                    .p100_img {
                        width: 100% !important;
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    /*! prevent replacing brackets */
                }

                @media only screen and (max-width: 640px) and screen and (-ms-high-contrast: active),
                only screen and (max-width: 640px) and (-ms-high-contrast: none) {

                    td,
                    th {
                        float: left;
                        width: 100%;
                        clear: both;
                    }

                    img:not(.p100_img),
                    .content-cell img {
                        width: auto;
                        height: auto;
                        max-width: 269px !important;
                        margin-right: auto;
                        display: block !important;
                        margin-left: auto;
                    }
                }

                .content-cell {
                    word-break: break-word;
                }

                .content-cell * {
                    -webkit-box-sizing: border-box;
                    box-sizing: border-box;
                }

                .rollover {
                    font-size: 0;
                }

                .rollover .rollover-second {
                    max-height: 0 !important;
                    display: none !important;
                }

                .rollover:hover .rollover-first {
                    max-height: 0 !important;
                    display: none !important;
                }

                .rollover:hover .rollover-second {
                    max-height: none !important;
                    display: block !important;
                    -o-object-fit: cover;
                    object-fit: cover;
                }

                #bodyTable table {
                    background: #f6f6f7;
                }

                @media only screen and (max-width: 640px) {
                    .sp-hidden-mob {
                        display: none !important;
                    }
                }
            </style>
            <table class="wrapper-table" cellpadding="5" cellspacing="0" width="100%" border="0"
                style="background-color:#ffffff;background-repeat:no-repeat;">
                <tbody>
                    <tr>
                        <td align="center">
                            <table cellpadding="0" cellspacing="0" width="600px" id="bodyTable" border="0" bgcolor="#f6f6f7">
                                <tbody>
                                    <tr>
                                        <td border="0" cellpadding="0" cellspacing="0">
                                            <table cellpadding="0" cellspacing="0" style="width:100%;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table class="separator" width="100%" cellpadding="0"
                                                                                cellspacing="0"
                                                                                style="border-collapse: collapse; padding-left:0px;padding-right:0px;padding-top:0px;padding-bottom:0px;height:30px;background-color:#ffffff;">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td height="30"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                style="height:39px;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell padding-lr-0 padding-bottom-0"
                                                                                            width="600" height="27"
                                                                                            style="padding-left:0px;padding-right:0px;padding-top:12px;padding-bottom:0px;">
                                                                                            <div id=""
                                                                                                style="width:100%;height:13;display:block;text-align:center;">
                                                                                                <a class="link_img"
                                                                                                    href="turandot-palace.ru">
                                                                                                    <center><img border="0"
                                                                                                            width="135" height="13"
                                                                                                            class=" sp-img small_img "
                                                                                                            align="center"
                                                                                                            alt="TURANDOT_LOGO__NEW_-_kopiya"
                                                                                                            src="https://s724266.sendpul.se/files/emailservice/userfiles/7fe1680e18920d765262308f17943b08724266/TVR/TURANDOT_LOGO__NEW_-_kopiya.png"
                                                                                                            style="display:block;-ms-interpolation-mode:bicubic;">
                                                                                                    </center>
                                                                                                </a>
                                                                                            </div>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <div class="block-divider"
                                                                                style="padding-left:0px;padding-right:0px;padding-top:0px;padding-bottom:0px;">
                                                                                <hr id=""
                                                                                    style="border-top-style:solid;border-top-width:1px;border-top-color:#3d3d3d;border-bottom:0; border-left:0;border-right:0;">
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%;text-align:left!impostant;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                id="w"
                                                                                style="text-color:black;font-weight:normal;margin:0;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell" width="556"
                                                                                            style="padding-left:28px;padding-right:16px;padding-top:7px;padding-bottom:5px;">
                                                                                            <p
                                                                                                style="font-weight:normal;line-height:1.2;padding:0;">
                                                                                                <span style="font-size: 36px;"><b style="box-sizing:border-box;width: 100%;display: block;text-align: center;">""" + name + """,
                                                                                                        поздравляем!</b></span>
                                                                                            </p>
                                                                                                <span style="font-weight: 400;">
                                                                                                    <p style="text-align:left!important;">Вы приобрели 
                                                                                                        """ + name_cert + """ №""" + code + """
                                                                                                        номиналом """ + price + """&nbsp;руб.
                                                                                                    </p>
                                                                                                    <p style="text-align:left!important;">Вы можете воспользоваться им
                                                                                                        в течение года с момента
                                                                                                        покупки (<a href="https://turandotpalace.ru/static/politic/">условия
                                                                                                            покупки и
                                                                                                            использования</a>).</p>
                                                                                                    <p style="text-align:left!important;">
                                                                                                        При посещении ресторана
                                                                                                        предъявите персоналу QR-code
                                                                                                        (куаркод).
                                                                                                    </p>
                                                                                                    <p style="text-align:left!important;">С нетерпением ждем вас в
                                                                                                        гости! <br>
                                                                                                        Не забудьте предварительно
                                                                                                        забронировать стол. <br><br>
                                                                                                        С уважением, команда
                                                                                                        ресторана «Турандот» <br>
                                                                                                        Москва, Тверской бульвар, 26
                                                                                                        <br>
                                                                                                        welcome@turandot-palace.ru
                                                                                                        <br>
                                                                                                        +7 (495) 739-00-11</p>
                                                                                                </span>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                id="wout_block_29_element_0">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell" width="570"
                                                                                            style="padding-left:15px;padding-right:15px;padding-top:15px;padding-bottom:15px;">
                                                                                            <div id="wout_block_29_element_0"
                                                                                                style="width:100%;height:380;display:block;">
                                                                                                <img border="0" width="570"
                                                                                                    height="380" class=" sp-img "
                                                                                                    align="left"
                                                                                                    alt="Rihter_veb-afisha"
                                                                                                    src="https://turandotpalace.ru/qrimg/""" + code + """.png"
                                                                                                    iout_block_29_element_0=""
                                                                                                    style="display:block;-ms-interpolation-mode:bicubic;">
                                                                                            </div>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                id="w"
                                                                                style="text-color:black;font-weight:normal;margin:0;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell padding-top-0 padding-bottom-0"
                                                                                            width="540"
                                                                                            style="padding-left:30px;padding-right:30px;padding-top:0px;padding-bottom:0px;">
                                                                                            <p
                                                                                                style="text-align:center;font-weight:normal;padding:0;">
                                                                                                <span
                                                                                                    style="font-size: 13px; line-height: 19.5px;"><br>©
                                                                                                    Copyright, 2021, ресторан
                                                                                                    "Турандот"&nbsp;</span>
                                                                                            </p>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                style="size:32px;order:1;text-align:center;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell padding-lr-0 padding-top-0 padding-bottom-0"
                                                                                            width="600"
                                                                                            style="padding-left:0px;padding-right:0px;padding-top:0px;padding-bottom:0px;">
                                                                                            <table class="social" cellpadding="5"
                                                                                                border="0" cellspacing="0"
                                                                                                style="display:inline-block;border-spacing:0px;">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <th
                                                                                                            class="social_element social_element_h_i">
                                                                                                            <a href="https://www.facebook.com/Turandot.Restaurant/"
                                                                                                                style="text-decoration:none"><img
                                                                                                                    border="0"
                                                                                                                    alt="Facebook"
                                                                                                                    class="social small_img smallImg"
                                                                                                                    style="margin:5px"
                                                                                                                    vspace="5"
                                                                                                                    hspace="5"
                                                                                                                    title="Facebook"
                                                                                                                    width="32"
                                                                                                                    height="32"
                                                                                                                    src="https://s724266.sendpul.se/img/constructor/social/outlined/facebook.png"></a>
                                                                                                        </th>
                                                                                                        <th
                                                                                                            class="social_element social_element_h_i">
                                                                                                            <a href=""
                                                                                                                style="text-decoration:none"><img
                                                                                                                    border="0"
                                                                                                                    alt="Instagram"
                                                                                                                    class="social small_img smallImg"
                                                                                                                    style="margin:5px"
                                                                                                                    vspace="5"
                                                                                                                    hspace="5"
                                                                                                                    title="Instagram"
                                                                                                                    width="32"
                                                                                                                    height="32"
                                                                                                                    src="https://s724266.sendpul.se/img/constructor/social/outlined/instagram.png"></a>
                                                                                                        </th>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:#ffffff;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                id="w"
                                                                                style="text-color:black;background: #f6f6f7;;font-weight:normal;margin:0;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell padding-top-0 padding-bottom-0"
                                                                                            width="540"
                                                                                            style="padding-left:30px;padding-right:30px;padding-top:0px;padding-bottom:0px;">
                                                                                            <p
                                                                                                style="font-weight:normal;padding:0;">
                                                                                                <span
                                                                                                    style="font-size: 13px; line-height: 19.5px;">Вы
                                                                                                    получили это письмо, потому что
                                                                                                    подписаны на рассылки
                                                                                                    от&nbsp;</span><span
                                                                                                    style="font-size: 13px;">Ресторан
                                                                                                    "Турандот"</span><span
                                                                                                    style="font-size: 13px; color: inherit; line-height: inherit;">.</span>
                                                                                            </p>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table cellpadding="0" cellspacing="0" style="width:100%;" border="0">
                                                <tbody>
                                                    <tr>
                                                        <th width="600" style="vertical-align:top" cellpadding="0" cellspacing="0"
                                                            class="tc">
                                                            <table border="0" width="100%" cellpadding="0" cellspacing="0"
                                                                style="background-color:transparent;">
                                                                <tbody>
                                                                    <tr>
                                                                        <td cellpadding="0" cellspacing="0">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                id="w"
                                                                                style="text-color:black;background-color:transparent;font-weight:normal;margin:0;">
                                                                                <tbody>
                                                                                    <tr class="content-row">
                                                                                        <td class="content-cell" width="570"
                                                                                            style="padding-left:15px;padding-right:15px;padding-top:10px;padding-bottom:6px;">
                                                                                            <p
                                                                                                style="text-align:center;font-weight:normal;padding:0;">
                                                                                                <span
                                                                                                    style="text-decoration: underline; color: #808080;"><a
                                                                                                        href="http://s724266.sendpul.se/unsubscribes/ru/{{CampaignId}}/{{EmailCode}}/h/e5203e703e95d001c286990c45fc87ee">Отписаться</a></span>
                                                                                            </p>
                                                                                            <div style="clear: both"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <table width="600px"></table>
                        </td>
                    </tr>
                </tbody>
            </table>

            </html>
        """

        msg = email.message.Message()
        msg['Subject'] = name_cert

        msg['From'] = "####"
        msg['To'] = mail
        password = "####"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        s = smtplib.SMTP('####')
        s.starttls()

        # Login Credentials for sending the mail
        s.login(msg['From'], password)

        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    def message_true_service(code, name_cert, clientid, price, mail, phone):

        text = (f"Был приобретен {name_cert} №{code} номиналом {price}&nbsp;руб. <br>"
                f"Данные покупателя: <br>"
                f"{clientid} <br>"
                f"{phone} <br>"
                f"{mail} <br>")
        email_content = '<html><head></head><body><p>' + text + '</p></body></html>'

        msg = email.message.Message()
        msg['Subject'] = f'Приобретен {name_cert} №{code}'

        msg['From'] = "####"
        msg['To'] = "####"
        password = "####"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        s = smtplib.SMTP('####')
        s.starttls()

        # Login Credentials for sending the mail
        s.login(msg['From'], password)

        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))        

