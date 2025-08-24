/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";
import { onWillStart ,onWillRender} from "@odoo/owl";
import {_t} from "@web/core/l10n/translation";

patch(ListRenderer.prototype, {
    setup(){
        super.setup();
        if (this.props.nestedKeyOptionalFieldsData) {
            onWillRender(() => {
                if (["sale.order", "purchase.order"].includes(this.props.nestedKeyOptionalFieldsData?.model)){
                    const datas = this.env.model.root.data;
                    // console.log("State berubah:", datas?.state);

                    if (datas && datas.state !== "draft") {
                        this.creates = [];
                    }
                    else{
                        this.creates = this.props.archInfo.creates.length
                    ? this.props.archInfo.creates
                    : [{ type: "create", string: _t("Add a line") }];
                    }
                }
            })
        }
    }
});
