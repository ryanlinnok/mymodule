odoo.define('rlk_x2many_list.form_relational', function (require) {
    "use strict";

    var core = require('web.core');
    var ListView = require('web.ListView');
    var _t = core._t;

    ListView.List.include({
        pad_table_to: function (count) {
            this._super.apply(this, arguments);

            var self = this;
            var parent_view = self.view.dataset.parent_view;
            var isDraft = true; // Default true, tampilkan jika tidak ada parent atau bukan model yang dicari

            if (parent_view) {
                var parent_model = parent_view.model;
                var parent_data = parent_view.datarecord;

                // if (parent_model === 'sale.order') {
                if (parent_data && parent_data.state) { // Pastikan parent_data dan state ada
                    isDraft = parent_data.state === 'draft';
                    }
                // }
            }

            if (!isDraft) {
                setTimeout(function () {
                    self.$current.find('.o_form_field_x2many_list_row_add').css('display', 'none');
                }, 0);
            }
        },
    });

    return {};
});
