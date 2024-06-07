/** @odoo-module **/
/*
Copyright 2024 Awartono
*/

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { capitalize } from "@web/core/utils/strings";
import { ErrorDialog, ClientErrorDialog, NetworkErrorDialog, WarningDialog, RedirectWarningDialog } from "@web/core/errors/error_dialogs";
import { patch } from "@web/core/utils/patch";

patch(ErrorDialog.prototype, {
    setup() {
        ErrorDialog.title = _t("Error");
        return super.setup();
    }
});

patch(ClientErrorDialog.prototype, {
    setup() {
        ClientErrorDialog.title = _t("Client Error");
        return super.setup();
    }
});

patch(NetworkErrorDialog.prototype, {
    setup() {
        NetworkErrorDialog.title = _t("Network Error");
        return super.setup();
    }
});

patch(WarningDialog.prototype, {
    inferTitle() {
        if (this.props.exceptionName && odooExceptionTitleMap.has(this.props.exceptionName)) {
            return odooExceptionTitleMap.get(this.props.exceptionName).toString();
        }
        return this.props.title || _t("Warning");
    }
});

patch(RedirectWarningDialog.prototype, {
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

