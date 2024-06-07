/** @odoo-module **/
/*
Copyright 2024 Awartono
*/

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { capitalize } from "@web/core/utils/strings";

import { RedirectWarningDialog } from "@web/core/errors/error_dialogs";
import { patch } from "@web/core/utils/patch";

const component = { RedirectWarningDialog };
patch(component.RedirectWarningDialog.prototype, {
    setup() {
        this.actionService = useService("action");
        const { data, subType } = this.props;
        const [message, actionId, buttonText, additionalContext] = data.arguments;
        this.title = capitalize(subType) || _t("Warning");
        this.message = message;
        this.actionId = actionId;
        this.buttonText = buttonText;
        this.additionalContext = additionalContext;
    }
});
