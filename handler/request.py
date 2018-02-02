from flask import jsonify
from dao.request import RequestDAO
from dao.product import ProductDAO

class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_pname'] = row[1]
        result['r_qty'] = row[2]
        result['r_date'] = row[3]
        result['pin_id'] = row[4]
        result['pin_fname'] = row[5]
        result['pin_lname'] = row[6]
        return result


    def build_dict(self, row):
        result = {}
        result['pin_fname'] = row[0]
        result['pin_lname'] = row[1]
        result['r_pname'] = row[2]
        result['r_qty'] = row[3]
        result['r_date'] = row[4]
        return result

    def build_product(self, row):
        result = {}
        result['pr_id'] = row[0]
        result['pr_name'] = row[1]
        result['pr_qty'] = row[2]
        result['pr_unit'] = row[3]
        result['pr_category'] = row[4]
        result['pr_priceperunit'] = row[5]
        return result

    def build_pin_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['p_fname'] = row[1]
        result['p_lname'] = row[2]
        result['p_street_apt_urb'] = row[3]
        result['p_city'] = row[4]
        result['p_zipcode'] = row[5]
        result['p_country'] = row[6]
        result['p_phone'] = row[7]
        return result

    def getAllRequest(self):
        dao = RequestDAO()
        request_list = dao.getAllRequest()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def browseResourcesRequested(self):
        dao = RequestDAO()
        request_list = dao.browseResourcesRequested()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def browseResourcesAvailable(self):
        dao = RequestDAO()
        request_list = dao.browseResourcesAvailable()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def searchProductByRequests(self, args):
        r_id = args.get("r_id")
        r_pname = args.get("r_pname")
        r_date = args.get("r_date")
        r_qty = args.get("r_qty")
        pin_id = args.get("pin_id")
        pin_fname = args.get("pin_fname")
        pin_lname = args.get("pin_lname")
        dao = RequestDAO()
        request_list = []
        if (len(args) == 1) and r_id:
            request_list = dao.GetRequestsByID(r_id)
        elif (len(args) == 1) and r_pname:
            request_list = dao.GetRequestsByPNAME(r_pname)
        elif (len(args) == 1) and r_date:
            request_list = dao.GetRequestsByDATE(r_date)
        elif (len(args) == 1) and r_qty:
            request_list = dao.GetRequestsByQTY(r_qty)
        elif (len(args) == 1) and pin_id:
            request_list = dao.GetRequestsByPINID(pin_id)
        elif (len(args) == 1) and pin_fname:
            request_list = dao.GetRequestsByPINFNAME(pin_fname)
        elif (len(args) == 2) and pin_fname and pin_lname:
            request_list = dao.GetRequestsByPINFULLNAME(pin_fname, pin_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)



    def insert_new_request(self, pin_id, r_pname, r_qty, r_date):
        dao = RequestDAO()
        r_id = dao.insert_new_request(pin_id, r_pname, r_qty, r_date)
        result = {}
        result["Request Id"] = r_id
        result["Person Id"] = pin_id
        result["Product Name"] = r_pname
        result["Quantity"] = r_qty
        result["Date"] = r_date
        return result


