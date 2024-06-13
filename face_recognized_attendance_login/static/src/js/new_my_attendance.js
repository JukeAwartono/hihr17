/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";

patch(ActivityMenu.prototype, {
    setup () {
        this.orm = useService("orm");
        return super.setup();
    },
    async signInOut() {

        const login = await this.orm.call("hr.employee", "get_login_screen", []);
        console.log(login)

        if (login == 1) {
            return super.signInOut();
        } else if (login == 3) {
            window.alert("Employee image path not set!")
        } 
        else{
            window.alert("Failed to recognize the face. Please try again....")
        }
        // return super.setup();

    }
})