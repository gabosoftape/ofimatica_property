===========================================
Property Management
===========================================
.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3


Features:




Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/dhongu/deltatech/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======


Contributors
------------

* Gabriel Pabon <gabosoft.ape@gmail.com>


Maintainer
----------

This module is maintained by the Ofimatica Soluciones.
<page string="Property Details" name="Property Details">
                    <group>
                        <group style="width:50%">
                            <group string="About Property" style="width:100%">
                                <field name="current_property_user_id" invisible="1"/>
                                <div>
                                <label for="property_price" string="Property Price" attrs="{'invisible': [('property_for','=','rent')]}"/>
                                <label for="property_price" string="Expected Rent" attrs="{'invisible': [('property_for','=','sale')]}"/>
                                </div>
                                <field name="property_price" widget="monetary" required="1" nolabel="1" style="width:80%"/>
                                <field name="is_price_negotiable"/>
                                <field name="partner_id"/>
                                <field name="property_for" required="1"/>
                                <field name="property_type" required="1"/>
                                <field name="residential_property" attrs="{'invisible': [('property_type', '!=', 'residential')]}"/>
                                <field name="commercial_property" attrs="{'invisible': [('property_type', '!=', 'commercial')]}"/>
                                <label for="maintenance_charge" string="Maintenance Charge" attrs="{'invisible': [('property_for','!=','rent'),('property_type', '=', 'residential')]}"/>
                                <div attrs="{'invisible': [('property_for','!=','rent'),('property_type', '=', 'residential')]}">
                                  <field name="maintenance_charge" style="width:50%"/>
                                  <field name="maintenance_charge_type" nolabel="1" style="width:50%"/>
                                </div>
                                <field name="deposit" attrs="{'invisible': [('property_for','!=','rent')]}"/>
                                <field name="is_pg_accomodation" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('property_for', '!=', 'rent')]}"/>
                                <label for="is_pg_for_girls" string="PG available for" attrs="{'invisible': [('is_pg_accomodation','!=',True)]}"/>
                                <div attrs="{'invisible': [('is_pg_accomodation','!=',True)]}">
                                    <field name="is_pg_for_girls" nolabel="1"/> <label for="is_pg_for_girls" string="Girls"/>
                                    <field name="is_pg_for_boys" nolabel="1"/> <label for="is_pg_for_boys" string="Boys"/>
                                    <field name="is_pg_for_all" nolabel="1"/> <label for="is_pg_for_all" string="All"/> <br/>
                                    <field name="is_tenant_students" nolabel="1"/> <label for="is_tenant_students" string="Students"/>
                                    <field name="is_tenant_working" nolabel="1"/> <label for="is_tenant_working" string="Working"/>
                                </div>
                                <label for="is_family" string="Willing to rent out to" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('property_for', '!=', 'rent')]}"/>
                                <div attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('property_for', '!=', 'rent')]}">
                                    <field name="is_family" nolabel="1"/> <label for="is_family" string="Family"/> <br/>
                                    <field name="is_single_man" nolabel="1"/> <label for="is_single_man" string="Single Man"/> <br/>
                                    <field name="is_single_woman" nolabel="1"/> <label for="is_single_woman" string="Single Woman"/>
                                </div>
                                <field name="new_or_resale" attrs="{'invisible': [('property_for', '=', 'rent')]}"/>
                                <label for="street" string="Location"/>
                                <div class="o_address_format">
                                    <field name="street" placeholder="Street..." class="o_address_street"/>
                                    <field name="street2" placeholder="Street 2..." class="o_address_street"/>
                                    <field name="city" placeholder="City" class="o_address_city"/>
                                    <field name="state_id" class="o_address_state" placeholder="State" options="{&quot;no_open&quot;: True}"/>
                                    <field name="zip" placeholder="ZIP" class="o_address_zip"/>
                                    <field name="country_id" placeholder="Country" class="o_address_country" options="{&quot;no_open&quot;: True, &quot;no_create&quot;: True}"/>
                                </div>
                            </group><br/>
                            <group string="Property Area" style="width:100%">
                                <field name="built_up_area" attrs="{'invisible': [('residential_property', '==', 'plot')]}"/>
                                <field name="carpet_area" attrs="{'invisible': [('residential_property', '==', 'plot')]}"/>
                                <field name="total_floors" attrs="{'invisible': [('residential_property', '==', 'plot')]}"/>
                                <field name="property_floors" attrs="{'invisible': [('residential_property', '==', 'plot')]}"/>
                                <field name="plot_area" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            </group>
                        </group>
                        <group string="Property Details" style="width:50%">
                            <field name="allowed_installments" widget="many2many_tags" attrs="{'invisible': [('property_for', '=', 'rent')]}"/>
                            <field name="bedrooms" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <field name="bathrooms" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <field name="balconies" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <field name="furnishing" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <label string="Additional Rooms" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <div attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}">
                                <field name="is_pooja_room"/> <label for="is_pooja_room" string="Pooja Room"/> <br/>
                                <field name="is_study_room"/> <label for="is_study_room" string="Study Room"/> <br/>
                                <field name="is_servant_room"/> <label for="is_servant_room" string="Servant Room"/> <br/>
                                <field name="is_other_room"/> <label for="is_other_room" string="Other Room"/> <br/>
                            </div>
                            <label string="Property Amenities" attrs="{'invisible': [('residential_property','==','plot')]}"/>
                            <div attrs="{'invisible': [('residential_property','==','plot')]}">
                                <field name="is_piped_gas"/> <label for="is_piped_gas" string="Piped Gas"/> <br/>
                                <field name="is_air_conditioned"/> <label for="is_air_conditioned" string="Air Conditioned"/><br/>
                                <field name="is_internet_wifi"/> <label for="is_internet_wifi" string="Internet Wifi Connectivity"/><br/>
                              <div attrs="{'invisible': [('property_type','==','residential')]}">
                                <label for="washrooms" string="Washrooms:"/><field name="washrooms"/><br/>
                                <field name="is_waste_disposal"/> <label for="is_waste_disposal" string="Waste Disposal"/> <br/>
                                <field name="is_banquet_hall"/> <label for="is_banquet_hall" string="Banquet Hall"/> <br/>
                                <field name="is_powerback_up"/> <label for="is_powerback_up" string="Powerback up"/> <br/>
                                <field name="is_food_court"/> <label for="is_food_court" string="Food Court"/> <br/>
                                <field name="is_conference_room"/> <label for="is_conference_room" string="Conference room"/> <br/>
                                <field name="is_security_alarm"/> <label for="is_security_alarm" string="Security Alarm"/> <br/>
                                <field name="is_water_storage"/> <label for="is_water_storage" string="Water Storage"/> <br/>
                                <field name="is_bar_or_lounge"/> <label for="is_bar_or_lounge" string="Bar/Lounge"/> <br/>
                                <field name="is_shopping_center"/> <label for="is_shopping_center" string="Shopping Center"/> <br/>
                                <field name="is_corner_property"/> <label for="is_corner_property" string="Corner Property"/> <br/>
                              </div>
                            </div>
                            <field name="plot_facing" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            <field name="allowed_construction_floors" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            <field name="facing_road_width" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            <field name="is_corner_property" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            <field name="boundry_wall_mad" widget="radio" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                            <label string="Society Amenities" attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}"/>
                            <div attrs="{'invisible': ['|',('property_type', '!=', 'residential'),('residential_property','==','plot')]}">
                                <field name="is_lifts"/> <label for="is_lifts" string="Lifts"/>
                                <field name="is_parks"/> <label for="is_parks" string="Parks"/>
                                <field name="is_security"/> <label for="is_security" string="Security"/><br/>
                                <field name="is_swimming_pool"/> <label for="is_swimming_pool" string="Swimming Pool"/><br/>
                                <field name="is_visitor_parking"/><label for="is_visitor_parking" string="Visitors Parking"/><br/>
                                <field name="is_maintenance_staff"/> <label for="is_maintenance_staff" string="Maintenance Staff"/> <br/>
                                <field name="is_fitness_center"/><label for="is_fitness_center" string="Fitness Center/Gym"/><br/>
                            </div>
                            <field name="plot_facing" attrs="{'invisible': [('residential_property', '!=', 'plot')]}"/>
                        </group>
                    </group>
                    <group>
                        <group string="Property Availibility">
                            <field name="is_propery_available" widget="radio" nolabel="1" attrs="{'invisible': [('property_for','=','rent')]}"/>
                            <field name="property_age" attrs="{'invisible': [('property_for','=','sale')]}"/>
                            <field name="property_available_form" attrs="{'invisible': [('property_for','=','sale')]}"/>
                            <field name="ownership"/>
                        </group>
                        <group string="Reserved Parking" attrs="{'invisible': [('residential_property','==','plot')]}">
                            <field name="is_parking"/>
                            <field name="open_parking" style="width:50%"/>
                            <field name="covered_parking" style="width:50%"/>
                        </group><br/>
                        <group style="width:100%">
                            <field name="property_description" required="1"/>
                        </group>
                    </group>
                </page>s

