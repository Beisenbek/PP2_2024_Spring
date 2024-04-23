import psycopg2

def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"

    # statement for inserting a new row into the vendor_parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id,part_id) VALUES(%s,%s)"

    conn = None

    try:
        with psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="123") as conn:
            with conn.cursor() as cur:
                # insert a new part
                cur.execute(insert_part, (part_name,))

                # get the part id
                row = cur.fetchone()
                if row:
                    part_id = row[0]
                else:
                    raise Exception('Could not get the part id')
                

                print(row[0])
                
                # assign parts provided by vendors
                for vendor_id in vendor_list:
                    cur.execute(assign_vendor, (vendor_id, part_id))

                # commit the transaction
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()

        print(error)

if __name__ == '__main__':
    add_part('Power Amplifier', (99,))