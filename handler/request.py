from flask import jsonify
from dao.request import RequestDAO

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

    def build_request2_dict(self, r_id, r_pname, r_qty, r_date, pin_id):
        result = {}
        result['r_id'] = r_id
        result['r_pname'] = r_pname
        result['r_qty'] = r_qty
        result['r_date'] = r_date
        result['pin_id'] = pin_id
        return result

    def getAllRequest(self):
        dao = RequestDAO()
        request_list = dao.getAllRequest()
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

    def insert_request(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            pin_id = form['pin_id']
            r_pname = form['r_pname']
            r_qty = form['r_qty']
            r_date = form['r_date']
            if pin_id and r_pname and r_date and r_qty:
                dao = RequestDAO()
                r_id = dao.insert_new_request(pin_id, r_pname, r_qty, r_date)
                result = self.build_request2_dict(r_id, r_pname, r_qty, r_date, pin_id)
                return jsonify(NewRequest=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateRequest(self, r_id, form):
        dao = RequestDAO()
        if not dao.GetRequestsByID(r_id):
            return jsonify(Error="Request not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                pin_id = form['pin_id']
                r_pname = form['r_pname']
                r_qty = form['r_qty']
                r_date = form['r_date']
                if pin_id and r_pname and r_date and r_qty:
                    dao.update_request(r_id, pin_id, r_pname, r_date, r_qty)
                    result = self.build_request2_dict(r_id, r_pname, r_qty, r_date, pin_id)
                    return jsonify(UpdatedRequest=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

